import logging
import time
import csv
import io

import pandas as pd
import math

from django.db.models import Q
from django.db import connection
from django.db.models.query import Prefetch
from django.http.response import HttpResponse, HttpResponseForbidden, HttpResponseNotAllowed
from django.http import HttpResponseServerError, JsonResponse, HttpResponseNotFound
from django.core.paginator import Paginator
from rest_framework import viewsets, filters, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny
from rest_framework.decorators import action, api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from . import models, serializers
from .permissions import CanReleaseResultsPermission
from .regex import SINGLE_TERM_QUERIES, MULTI_TERM_QUERIES

# Get an instance of a logger
logger = logging.getLogger(__name__)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class GeneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing/editing Genes.
    """
    pagination_class = StandardResultsSetPagination
    queryset = models.Genes.objects.all().order_by('approved_symbol')
    serializer_class = serializers.GeneSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('approved_symbol', 'approved_name', 'alias_symbols')

    @action(detail=False, permission_classes=[permissions.AllowAny], url_path='symbol/(?P<symbol>[^/]+)', url_name='symbol')
    def get_by_symbol(self, request, *args, **kwargs):
        start = time.time()
        symbol = kwargs['symbol']
        instance = models.Genes.objects.filter(approved_symbol=symbol).prefetch_related(
                                                                        Prefetch('annotations', queryset=models.GeneAnnotation.objects.filter(gene__approved_symbol=symbol)),
                                                                        ).first()
        if instance:
            print(f"Number of queries pre-serialization: {len(connection.queries)}")
            serializer_start = time.time()
            serializer = serializers.GeneWithAnnotationSerializer(instance, context={'request': request}, many=False)
            #serializer = serializers.FullGeneSerializer(instance, context={'request': request}, many=False)
            data = serializer.data
            serializer_time = time.time() - serializer_start
            print(f"Serializer time: {serializer_time}")
            print(f"Number of queries post-serialization: {len(connection.queries)}")
            time_diff = time.time() - start
            print(f"Full queryset time: {time_diff}")
            return Response(data)
        else:
            return HttpResponseNotFound('No gene associated with that symbol.')


class GeneAnnotationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing/editing Analysis Types.
    """
    queryset = models.GeneAnnotation.objects.all()
    serializer_class = serializers.GeneAnnotationSerializer
    permission_classes = (permissions.AllowAny, )

    def create(self, request):
        self.serializer_class = serializers.ScoredGeneAnnotationSerializer
        if hasattr(request.data, '_mutable'):
            _mutable = request.data._mutable
            request.data._mutable = True
            request.data['user'] = request.user.id
            request.data._mutable = _mutable
            return super().create(request)
        if request.user and hasattr(request.user, 'affiliation_id') and request.user.affiliation_id.abbr != 'DDB':
            request.data['user'] = request.user.id
        if 'score' in request.data:
            del request.data['score']
        return super().create(request)

    @action(detail=False, permission_classes=[IsAuthenticated, CanReleaseResultsPermission], url_path='export', url_name='export')
    def export(self, request, *args, **kwargs):
        """
        API endpoint that creates a dummy analysis record with info from DaveLab.
        """
        annotations = models.GeneAnnotation.objects.prefetch_related('gene', 'user')
        serializer_start = time.time()
        logger.info(f"Number of queries pre-serialization: {len(connection.queries)}")
        serializer = serializers.GeneAnnotationExportSerializer(annotations, context={'request': request}, many=True)
        data = serializer.data
        serializer_time = time.time() - serializer_start
        logger.info(f"Serializer time: {serializer_time}")
        logger.info(f"Number of queries post-serialization: {len(connection.queries)}")
        return Response(data)


class VariantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing/editing Variants.
    """
    pagination_class = StandardResultsSetPagination
    queryset = models.Variants.objects.all().order_by('chrom_pos_ref_alt')
    serializer_class = serializers.VariantSearchSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('chrom_pos_ref_alt', 'refseq_hgvsg_id', 'alt_hgvsg_id', 'hgvsg_id', 'lrg_hgvsg_id', 'transcripts__ensembl_transcript_id')

    @action(detail=False, permission_classes=[permissions.AllowAny], url_path='missing-annovar', url_name='missing_annovar')
    def get_missing_annovar_file(self, request, *args, **kwargs):
        start = time.time()
        chromosome = request.GET.get('chr', None)
        filter = Q()
        if chromosome:
            filter = Q(chr=chromosome)
            filter.add(Q(alt_chr=chromosome), Q.OR)
        filter.add(Q(annovar__isnull=True), Q.AND)
        variants = models.Variants.objects.filter(filter).order_by('chrom_pos_ref_alt')
        if variants.exists():
            try:
                csv_rows = [[str(row.chr), str(row.start_pos), str(row.end_pos), str(row.ref_allele), str(row.alt_allele)] for row in variants]
                csv_rows.insert(0, ["#CHROM", "START", "END", "REF", "ALT"])
                # for row in variants.iterator():
                #     csv_rows.append([str(row.chr), str(row.start_pos), str(row.end_pos), str(row.ref_allele), str(row.alt_allele)])
                buffer = io.StringIO()
                wr = csv.writer(buffer, quoting=csv.QUOTE_NONE, delimiter='\t', quotechar='', escapechar='\\')
                wr.writerows(csv_rows)
                buffer.seek(0)
                response = HttpResponse(buffer, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename=missing_annovar.tsv'

                time_diff = time.time() - start
                print(f"Full endpoint execution time: {time_diff}")

                return response
            except Exception as e:
                logger.error("Download missing annovar exception: %s", e)
                time_diff = time.time() - start
                print(f"Full endpoint execution time: {time_diff}")
                return Response({"responseType": "error", "message": "Failed to get variants with missing annovar data"})
        else:
            return Response({"responseType": "success", "message": "No variants with missing records!"})

    @action(detail=False, permission_classes=[permissions.AllowAny], url_path='cpra/(?P<cpra>[^/]+)', url_name='cpra')
    def get_by_chrom_pos_ref_alt(self, request, *args, **kwargs):
        start = time.time()
        cpra = kwargs['cpra']
        instance = models.Variants.objects.filter(chrom_pos_ref_alt=cpra).prefetch_related(
                                                                        Prefetch('amino_acid_changes', queryset=models.AminoAcidChange.objects.filter(variants__chrom_pos_ref_alt=cpra).distinct()),
                                                                        'gene',
                                                                        Prefetch('amino_acid_changes__transcript', queryset=models.Transcript.objects.filter(variants__chrom_pos_ref_alt=cpra).distinct()),
                                                                        'amino_acid_changes__annotations',
                                                                        Prefetch('amino_acid_changes__genes', queryset=models.Genes.objects.filter(variants__chrom_pos_ref_alt=cpra).distinct()),
                                                                        'gene__annotations'
                                                                        ).first()
        if instance:
            print(f"Number of queries pre-serialization: {len(connection.queries)}")
            serializer_start = time.time()
            serializer = serializers.VariantTranscriptSerializer(instance, context={'request': request}, many=False)
            data = serializer.data
            serializer_time = time.time() - serializer_start
            print(f"Serializer time: {serializer_time}")
            print(f"Number of queries post-serialization: {len(connection.queries)}")
            time_diff = time.time() - start
            print(f"Full queryset time: {time_diff}")
            return Response(data)
        else:
            return HttpResponseNotFound('No variant associated with that Chrom-Pos-Ref-Alt.')

    @action(detail=False, permission_classes=[permissions.AllowAny], url_path='transcripts/(?P<cpra>[^/]+)/(?P<aa_change>[^/]+)', url_name='transcripts')
    def get_transcripts(self, request, *args, **kwargs):
        start = time.time()
        cpra = kwargs['cpra'].replace('chr', '')
        aa_change = str(kwargs['aa_change'])
        transcript_list = models.Transcript.objects.filter(aa_transcript_variants__variant__chrom_pos_ref_alt=cpra, aa_transcript_variants__amino_acid__short_name=aa_change)
        if transcript_list:
            print(f"Number of queries pre-serialization: {len(connection.queries)}")
            serializer_start = time.time()
            serializer = serializers.TranscriptSerializer(transcript_list, context={'request': request}, many=True)
            data = serializer.data
            serializer_time = time.time() - serializer_start
            print(f"Serializer time: {serializer_time}")
            print(f"Number of queries post-serialization: {len(connection.queries)}")
            time_diff = time.time() - start
            print(f"Full queryset time: {time_diff}")
            return Response(data)
        else:
            return JsonResponse([])

    @action(detail=False, permission_classes=[permissions.AllowAny], url_path='gene/(?P<symbol>[^/]+)', url_name='gene_variants')
    def get_gene_variants(self, request, *args, **kwargs):
        start = time.time()
        gene_symbol = kwargs['symbol']
        variant_list = models.Variants.objects.filter(gene__approved_symbol=gene_symbol).prefetch_related(
                                                                                        Prefetch('aa_transcript_variants', queryset=models.AminoAcidTranscriptVariant.objects.filter(variant__gene__approved_symbol=gene_symbol).distinct('amino_acid')),
                                                                                        Prefetch('aa_transcript_variants__amino_acid__genes', queryset=models.Genes.objects.filter(approved_symbol=gene_symbol).distinct())
                                                                                    )
        if variant_list:
            print(f"Number of queries pre-serialization: {len(connection.queries)}")
            serializer_start = time.time()
            serializer = serializers.GeneVariantAminoAcidSerializer(variant_list, context={'request': request}, many=True)
            data = serializer.data
            serializer_time = time.time() - serializer_start
            print(f"Serializer time: {serializer_time}")
            print(f"Number of queries post-serialization: {len(connection.queries)}")
            time_diff = time.time() - start
            print(f"Full queryset time: {time_diff}")
            return Response(data)
        else:
            return JsonResponse([])


class TranscriptViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing/editing Transcripts.
    """
    pagination_class = StandardResultsSetPagination
    queryset = models.Transcript.objects.all()
    serializer_class = serializers.TranscriptSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('ensembl_transcript_id',)


class AminoAcidChangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing/editing Amino Acid Changes.
    """
    pagination_class = StandardResultsSetPagination
    queryset = models.AminoAcidChange.objects.all()
    serializer_class = serializers.AminoAcidChangeSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('long_name','short_name',)

    @action(detail=False, permission_classes=[permissions.AllowAny], url_path='short_name/(?P<gene>[^/]+)/(?P<short_name>[^/]+)', url_name='short_name')
    def get_by_name(self, request, *args, **kwargs):
        start = time.time()
        gene = kwargs['gene']
        short_name = kwargs['short_name']
        instance = models.AminoAcidChange.objects.filter(short_name=short_name).prefetch_related(
                                                                        Prefetch('annotations', queryset=models.AminoAcidAnnotations.objects.all()),
                                                                        Prefetch('genes', queryset=models.Genes.objects.filter(approved_symbol=gene)),
                                                                        Prefetch('genes__annotations', queryset=models.GeneAnnotation.objects.all()),
                                                                        Prefetch('transcript', queryset=models.Transcript.objects.all()),
                                                                        Prefetch('variants', queryset=models.Variants.objects.filter(gene__approved_symbol=gene).distinct()),
                                                                        'variants__gene'
                                                                        ).first()
        if instance:
            print(f"Number of queries pre-serialization: {len(connection.queries)}")
            serializer_start = time.time()
            serializer = serializers.AminoAcidWithAnnotationsSerializer(instance, context={'request': request}, many=False)
            data = serializer.data
            serializer_time = time.time() - serializer_start
            print(f"Serializer time: {serializer_time}")
            print(f"Number of queries post-serialization: {len(connection.queries)}")
            time_diff = time.time() - start
            print(f"Full queryset time: {time_diff}")
            return Response(data)
        else:
            return HttpResponseNotFound('No amino acid change associated with that name.')


class AminoAcidAnnotationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing/editing Amino Acid Change Annotations.
    """
    queryset = models.AminoAcidAnnotations.objects.all()
    serializer_class = serializers.AminoAcidAnnotationSerializer
    permission_classes = (permissions.AllowAny, )

    def create(self, request):
        self.serializer_class = serializers.ScoredAminoAcidAnnotationSerializer
        if hasattr(request.data, '_mutable'):
            _mutable = request.data._mutable
            request.data._mutable = True
            request.data['user'] = request.user.id
            request.data._mutable = _mutable
            if request.user and request.user.affiliation_id.abbr != 'DDB':
                request.data['user'] = request.user.id
            return super().create(request)
        if request.user and hasattr(request.user, 'affiliation_id') and request.user.affiliation_id.abbr != 'DDB':
            request.data['user'] = request.user.id
        if 'score' in request.data:
            del request.data['score']
        return super().create(request)

    @action(detail=False, permission_classes=[IsAuthenticated, CanReleaseResultsPermission], url_path='export', url_name='export')
    def export(self, request, *args, **kwargs):
        """
        API endpoint that creates a dummy analysis record with info from DaveLab.
        """
        annotations = models.AAAnnotation.objects.prefetch_related('aa_change', 'user', 'aa_change__variants', 'aa_change__transcripts')
        serializer_start = time.time()
        logger.info(f"Number of queries pre-serialization: {len(connection.queries)}")
        serializer = serializers.AminoAcidAnnotationExportSerializer(annotations, context={'request': request}, many=True)
        data = serializer.data
        serializer_time = time.time() - serializer_start
        logger.info(f"Serializer time: {serializer_time}")
        logger.info(f"Number of queries post-serialization: {len(connection.queries)}")
        return Response(data)


class AlfaDataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing ALFA Data.
    """
    pagination_class = StandardResultsSetPagination
    queryset = models.AlfaData.objects.all().order_by('chrom_pos_ref_alt')
    serializer_class = serializers.AlfaDataSerializer

    @action(methods=['post'], detail=False, permission_classes=[], url_path='filtered-results', url_name="filtered_results")
    def filtered_results(self, request, *args, **kwargs):
        try:
            variant_list = request.data['filter']
            alfa = models.AlfaData.objects.filter(chrom_pos_ref_alt__in=variant_list)
            serializer = serializers.AlfaDataSerializer(alfa, context={'request': request}, many=True)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error while retrieving ALFA data. Error: {e}")
            return HttpResponseServerError('Error while retrieving ALFA data')


@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
@authentication_classes([])
@permission_classes([])
def search(request):
    """
    API endpoint that allows user to search for Genes and Variants
    """

    search_term = request.query_params.get('query', '')
    if search_term:
        search_terms = search_term.split(' ')
        # check if multiple search terms provided
        if len(search_terms) > 1:

            # check for gene and aa change query (e.g., BRAF V600E, BRAF Val600Glu)
            if SINGLE_TERM_QUERIES.get('gene').match(search_terms[0]) and \
                    SINGLE_TERM_QUERIES.get('aa_change').match(search_terms[1]):
                # get the search term for gene symbol
                gene = search_terms[0]
                # get the search term for amino acid change
                aa_change = search_terms[1]

                # query the `api_genes` model for given gene symbol
                gene_queryset = models.Genes.objects.filter(Q(approved_symbol__exact=gene) |
                                                            Q(alias_names__icontains=gene)).all()

                # fetch the data for a given gene symbol and amoni acid change
                gene_aa_change = models.AminoAcidChange.objects.filter(Q(long_name__exact=aa_change) |
                                                                       Q(short_name__exact=aa_change)).prefetch_related(Prefetch('genes', queryset=gene_queryset))

                # if the records found
                if gene_aa_change:
                    # serialize the queryset data
                    serializer = serializers.GeneAminoAcidSerializer(gene_aa_change, context={'request': request},
                                                                     many=True)
                    # prepare the data for response
                    data = serializer.data

                    return Response(data)
                else:
                    return HttpResponseNotFound('No records found.')
        else:
            search_term = search_terms[0]

            """check for the search terms against different query criteria"""

            # check for Gene Query (e.g., BRAF, TP53)
            if SINGLE_TERM_QUERIES.get('gene').match(search_term):
                # query the `Gene` table for approved gene symbol
                approved_symbol = models.Genes.objects.filter(approved_symbol__iexact=search_term).all()
                # check if the query returns results for given gene symbol
                if approved_symbol:
                    serializer = serializers.GeneSerializer(approved_symbol, context={'request': request}, many=True)
                    data = serializer.data
                    return Response(data)
                else:
                    # query the `Gene` table for alias gene symbols in case the approved symbol not return anything
                    alias_symbols = models.Genes.objects.filter(alias_symbols__icontains=search_term).all()
                    if alias_symbols:
                        # serialize the queryset data
                        serializer = serializers.GeneSerializer(alias_symbols, context={'request': request},
                                                                many=True)
                        # prepare the data for response
                        data = serializer.data
                        return Response(data)
                    else:
                        return HttpResponseNotFound('No gene associated with that symbol found.')

            # check for Genomic Coordinates Query (e.g., chr1:12345-43234)
            elif SINGLE_TERM_QUERIES.get('genomic_coordinates').match(search_term):

                # separate the search term to obtain query criteria
                chrom, pos = search_term.split(':')
                start_pos, end_pos = pos.split('-')
                chrom = chrom.replace("chr", "")

                # query the `Variants` table for chromosome, start and end positions
                variants = models.Variants.objects.filter(chr__exact=chrom, start_pos__gte=start_pos,
                                                          start_pos__lte=end_pos, end_pos__gte=start_pos,
                                                          end_pos__lte=end_pos).all()

                # check if the query returns results for given genomic coordinates
                if variants:
                    serializer = serializers.VariantSerializer(variants, context={'request': request}, many=True)
                    data = serializer.data
                    return Response(data)
                else:
                    return HttpResponseNotFound('No variants found for given genomic coordinates.')

            # check for chr-pos-ref-alt Query (e.g., chr1-1234-A-C)
            elif SINGLE_TERM_QUERIES.get('chr_pos_ref_alt').match(search_term):

                # replace `chr` string if there is any
                search_term = search_term.replace("chr", "")

                # query the `Variants` table for chromosome, start and end positions
                variants = models.Variants.objects.filter(chrom_pos_ref_alt__exact=search_term).all()

                # check if the query returns results for given genomic coordinates
                if variants:
                    serializer = serializers.VariantSerializer(variants, context={'request': request}, many=True)
                    data = serializer.data
                    return Response(data)
                else:
                    return HttpResponseNotFound('No variants found for given genomic coordinates.')

            else:
                return Response("Search term is not allowed!")
    else:
        return Response("No search terms provided!")


@api_view(['POST'])
@permission_classes((IsAuthenticated))
def annotation_data_upload(request):
    try:
        file_serializer = serializers.AnnotationDataFileSerializer(data=request.data)

        if file_serializer.is_valid():
            # valid file upload
            xls = pd.ExcelFile(request.FILES['file'], engine='openpyxl')
            feedback_items = process_annotation_file(xls)
            return Response({"message": "Successful import!", "feedback": feedback_items})
        else:
            return Response(file_serializer.errors)
    except:
        import traceback
        tb_string = traceback.format_exc()
        print(f"Annotation data upload error!\n {tb_string}")


def process_annotation_file(xls):
    feedback_items = []
    sheet_names = {s.lower(): s for s in xls.sheet_names}
    # if "annovar" in sheet_names:
    #     print("Processing Annovar Data")
    #     feedback_items.extend(process_annovar_data(pd.read_excel(xls, sheet_name=sheet_names["annovar"])))
    # if "gene_annotations" in sheet_names:
    #     print("Processing Gene Annotation Data")
    #     feedback_items.extend(process_gene_annotation_data(pd.read_excel(xls, sheet_name=sheet_names["gene_annotations"])))
    if "variant_annotations" in sheet_names:
        print("Processing Variant Annotation Data")
        feedback_items.extend(process_variant_annotation_data(pd.read_excel(xls, sheet_name=sheet_names["variant_annotations"])))
    return feedback_items


def process_gene_annotation_data(df):
    feedback_items = []
    # iterate over records in upload and build json data
    data = df.to_dict('records')
    gene_import_list = list(set([x['gene'] for x in data]))
    gene_list = models.Genes.objects.filter(approved_symbol__in=gene_import_list)
    gene_dict = {x.approved_symbol: x for x in gene_list}
    for row in data:
        refGene = row["gene"]
        gene = gene_dict[refGene] if refGene in gene_dict else None
        if not gene:
            row_value = f"{refGene} : {row['annotation']}"
            feedback_items.append({'sheet': 'gene_annotations', 'row_value': row_value, 'issue': "Specified gene does not exist in the system."})
            continue
        if row['annotation'] and isinstance(row['annotation'], str):
            annotation = row['annotation']
            already_exists = False
            for annot in gene.annotations.all():
                if annotation == annot:
                    already_exists = True
                    break
            if already_exists:
                continue
            annotation = models.GeneAnnotation()
            annotation.annotation = row['annotation']
            annotation.priority = row['Priority'] if 'Priority' in row and not math.isnan(row['Priority']) else 0
            annotation.gene = gene
            annotation.save()
    return feedback_items


def process_variant_annotation_data(df):
    feedback_items = []
    # iterate over records in upload and build json data
    data = df.to_dict('records')
    annotation_list = models.AAAnnotation.objects.all()
    annotation_dict = {x.annotation: x for x in annotation_list}
    aa_list = models.AminoAcidChange.objects.all()
    aa_dict = {str(x.gene+"_"+x.aa_change): x for x in aa_list}
    for row in data:
        annotation = None
        if row['annotation'] and isinstance(row['annotation'], str):
            annotation = annotation_dict[row['annotation']] if row['annotation'] in annotation_dict else None
            if not annotation:
                annotation = models.AAAnnotation()
                annotation.annotation = row['annotation']
                annotation.priority = 0
                annotation.save()
                annotation_dict[row['annotation']] = annotation
        gene = row["Gene.refGene"]
        change = row["AA_change"]
        priority = row["priority"] if 'priority' in row and not math.isnan(row['priority']) else 1
        aa_change = aa_dict[str(gene+"_"+change)] if str(gene+"_"+change) in aa_dict else None
        if not aa_change:
            aa_change = models.AminoAcidChange()
            aa_change.gene = gene
            aa_change.aa_change = change
            aa_change.priority = priority
            aa_change.save()
            aa_dict[str(gene+"_"+change)] = aa_change
        if annotation:
            annotation.aa_change.add(aa_change)


def process_annovar_data(df):
    feedback_items = []
    # iterate over records in upload and build json data
    data = df.to_dict('records')
    # all_chrom_pos = [x['CHROM_POS_REF_ALT'].replace("chr", "").replace("CHR", "") if 'CHROM_POS_REF_ALT' in x else x['chrom_pos_ref_alt'].replace("chr", "").replace("CHR", "") for x in data]
    # variants = models.Variants.objects.filter(chrom_pos_ref_alt__in=all_chrom_pos)
    # print(models.Variants.objects.filter(chrom_pos_ref_alt__in=all_chrom_pos).count())
    # variant_dict = {x.chrom_pos_ref_alt: x for x in variants}
    for row in data:
        chrom_pos = row['CHROM_POS_REF_ALT'] if 'CHROM_POS_REF_ALT' in row else row['chrom_pos_ref_alt']
        chrom_pos = chrom_pos.replace("chr", "").replace("CHR", "")
        variant = models.Variants.objects.filter(chrom_pos_ref_alt=chrom_pos).first() # variant_dict[chrom_pos]
        if variant:
            # add annovar data
            annovar_record = variant.annovar.first()
            if not annovar_record:
                annovar_record = models.AnnovarData()
                annovar_record.variant = variant
            annovar_record.func_ref_gene = row['Func.refGene'] if 'Func.refGene' in row else row['func_ref_gene']
            annovar_record.gene_ref_gene = row['Gene.refGene'] if 'Gene.refGene' in row else row['gene_ref_gene']
            annovar_record.gene_detail_ref_gene = row['GeneDetail.refGene'] if 'GeneDetail.refGene' in row else row['gene_detail_ref_gene']
            annovar_record.exonic_func_ref_gene = row['ExonicFunc.refGene'] if 'ExonicFunc.refGene' in row else row['exonic_func_ref_gene']
            annovar_record.aa_change_ref_gene = row['AAChange.refGene'] if 'AAChange.refGene' in row else row['aa_change_ref_gene']
            annovar_record.genomic_super_dups = row['genomicSuperDups'] if 'genomicSuperDups' in row else row['genomic_super_dups']
            annovar_record.ex_ac_all = row['ExAC_ALL'] if 'ExAC_ALL' in row else row['ex_ac_all']
            annovar_record.gnomad_exome_af_popmax = row['gnomad_exome_AF_popmax'] if 'gnomad_exome_AF_popmax' in row else row['gnomad_exome_af_popmax']
            annovar_record.gnomad_genome_af = row['gnomad_genome_AF'] if 'gnomad_genome_AF' in row else row['gnomad_genome_af']
            annovar_record.avsnp_150 = row['avsnp150'] if 'avsnp150' in row else row['avsnp_150']
            annovar_record.cosmic_91_coding = row['cosmic91_coding'] if 'cosmic91_coding' in row else row['cosmic_91_coding']
            annovar_record.cosmic_91_noncoding = row['cosmic91_noncoding'] if 'cosmic91_noncoding' in row else row['cosmic_91_noncoding']
            annovar_record.sift_score = row['SIFT_score'] if 'SIFT_score' in row else row['sift_score']
            annovar_record.sift_converted_rankscore = row['SIFT_converted_rankscore'] if 'SIFT_converted_rankscore' in row else row['sift_converted_rankscore']
            annovar_record.sift_pred = row['SIFT_pred'] if 'SIFT_pred' in row else row['sift_pred']
            annovar_record.polyphen_2_hdiv_score = row['Polyphen2_HDIV_score'] if 'Polyphen2_HDIV_score' in row else row['polyphen_2_hdiv_score']
            annovar_record.polyphen_2_hdiv_rankscore = row['Polyphen2_HDIV_rankscore'] if 'Polyphen2_HDIV_rankscore' in row else row['polyphen_2_hdiv_rankscore']
            annovar_record.polyphen_2_hdiv_pred = row['Polyphen2_HDIV_pred'] if 'Polyphen2_HDIV_pred' in row else row['polyphen_2_hdiv_pred']
            annovar_record.polyphen_2_hvar_score = row['Polyphen2_HVAR_score'] if 'Polyphen2_HVAR_score' in row else row['polyphen_2_hvar_score']
            annovar_record.polyphen_2_hvar_rankscore = row['Polyphen2_HVAR_rankscore'] if 'Polyphen2_HVAR_rankscore' in row else row['polyphen_2_hvar_rankscore']
            annovar_record.polyphen_2_hvar_pred = row['Polyphen2_HVAR_pred'] if 'Polyphen2_HVAR_pred' in row else row['polyphen_2_hvar_pred']
            annovar_record.lrt_score = row['LRT_score'] if 'LRT_score' in row else row['lrt_score']
            annovar_record.lrt_converted_rankscore = row['LRT_converted_rankscore'] if 'LRT_converted_rankscore' in row else row['lrt_converted_rankscore']
            annovar_record.lrt_pred = row['LRT_pred'] if 'LRT_pred' in row else row['lrt_pred']
            annovar_record.mutation_taster_score = row['MutationTaster_score'] if 'MutationTaster_score' in row else row['mutation_taster_score']
            annovar_record.mutation_taster_converted_rankscore = row['MutationTaster_converted_rankscore'] if 'MutationTaster_converted_rankscore' in row else row['mutation_taster_converted_rankscore']
            annovar_record.mutation_taster_pred = row['MutationTaster_pred'] if 'MutationTaster_pred' in row else row['mutation_taster_pred']
            annovar_record.mutation_assessor_score = row['MutationAssessor_score'] if 'MutationAssessor_score' in row else row['mutation_assessor_score']
            annovar_record.mutation_assessor_score_rankscore = row['MutationAssessor_score_rankscore'] if 'MutationAssessor_score_rankscore' in row else row['mutation_assessor_score_rankscore']
            annovar_record.mutation_assessor_pred = row['MutationAssessor_pred'] if 'MutationAssessor_pred' in row else row['mutation_assessor_pred']
            annovar_record.fathmm_score = row['FATHMM_score'] if 'FATHMM_score' in row else row['fathmm_score']
            annovar_record.fathmm_converted_rankscore = row['FATHMM_converted_rankscore'] if 'FATHMM_converted_rankscore' in row else row['fathmm_converted_rankscore']
            annovar_record.fathmm_pred = row['FATHMM_pred'] if 'FATHMM_pred' in row else row['fathmm_pred']
            annovar_record.provean_score = row['PROVEAN_score'] if 'PROVEAN_score' in row else row['provean_score']
            annovar_record.provean_converted_rankscore = row['PROVEAN_converted_rankscore'] if 'PROVEAN_converted_rankscore' in row else row['provean_converted_rankscore']
            annovar_record.provean_pred = row['PROVEAN_pred'] if 'PROVEAN_pred' in row else row['provean_pred']
            annovar_record.vest_3_score = row['VEST3_score'] if 'VEST3_score' in row else row['vest_3_score']
            annovar_record.vest_3_rankscore = row['VEST3_rankscore'] if 'VEST3_rankscore' in row else row['vest_3_rankscore']
            annovar_record.meta_svm_score = row['MetaSVM_score'] if 'MetaSVM_score' in row else row['meta_svm_score']
            annovar_record.meta_svm_rankscore = row['MetaSVM_rankscore'] if 'MetaSVM_rankscore' in row else row['meta_svm_rankscore']
            annovar_record.meta_svm_pred = row['MetaSVM_pred'] if 'MetaSVM_pred' in row else row['meta_svm_pred']
            annovar_record.meta_lr_score = row['MetaLR_score'] if 'MetaLR_score' in row else row['meta_lr_score']
            annovar_record.meta_lr_rankscore = row['MetaLR_rankscore'] if 'MetaLR_rankscore' in row else row['meta_lr_rankscore']
            annovar_record.meta_lr_pred = row['MetaLR_pred'] if 'MetaLR_pred' in row else row['meta_lr_pred']
            annovar_record.m_cap_score = row['M.CAP_score'] if 'M.CAP_score' in row else row['m_cap_score']
            annovar_record.m_cap_rankscore = row['M.CAP_rankscore'] if 'M.CAP_rankscore' in row else row['m_cap_rankscore']
            annovar_record.m_cap_pred = row['M.CAP_pred'] if 'M.CAP_pred' in row else row['m_cap_pred']
            annovar_record.revel_score = row['REVEL_score'] if 'REVEL_score' in row else row['revel_score']
            annovar_record.revel_rankscore = row['REVEL_rankscore'] if 'REVEL_rankscore' in row else row['revel_rankscore']
            annovar_record.mut_pred_score = row['MutPred_score'] if 'MutPred_score' in row else row['mut_pred_score']
            annovar_record.mut_pred_rankscore = row['MutPred_rankscore'] if 'MutPred_rankscore' in row else row['mut_pred_rankscore']
            annovar_record.cadd_raw = row['CADD_raw'] if 'CADD_raw' in row else row['cadd_raw']
            annovar_record.cadd_raw_rankscore = row['CADD_raw_rankscore'] if 'CADD_raw_rankscore' in row else row['cadd_raw_rankscore']
            annovar_record.cadd_phred = row['CADD_phred'] if 'CADD_phred' in row else row['cadd_phred']
            annovar_record.dann_score = row['DANN_score'] if 'DANN_score' in row else row['dann_score']
            annovar_record.dann_rankscore = row['DANN_rankscore'] if 'DANN_rankscore' in row else row['dann_rankscore']
            annovar_record.fathmm_mkl_coding_score = row['fathmm.MKL_coding_score'] if 'fathmm.MKL_coding_score' in row else row['fathmm_mkl_coding_score']
            annovar_record.fathmm_mkl_coding_rankscore = row['fathmm.MKL_coding_rankscore'] if 'fathmm.MKL_coding_rankscore' in row else row['fathmm_mkl_coding_rankscore']
            annovar_record.fathmm_mkl_coding_pred = row['fathmm.MKL_coding_pred'] if 'fathmm.MKL_coding_pred' in row else row['fathmm_mkl_coding_pred']
            annovar_record.eigen_coding_or_noncoding = row['Eigen_coding_or_noncoding'] if 'Eigen_coding_or_noncoding' in row else row['eigen_coding_or_noncoding']
            annovar_record.eigen_raw = row['Eigen.raw'] if 'Eigen.raw' in row else row['eigen_raw']
            annovar_record.eigen_pc_raw = row['Eigen.PC.raw'] if 'Eigen.PC.raw' in row else row['eigen_pc_raw']
            annovar_record.geno_canyon_score = row['GenoCanyon_score'] if 'GenoCanyon_score' in row else row['geno_canyon_score']
            annovar_record.geno_canyon_score_rankscore = row['GenoCanyon_score_rankscore'] if 'GenoCanyon_score_rankscore' in row else row['geno_canyon_score_rankscore']
            annovar_record.integrated_fit_cons_score = row['integrated_fitCons_score'] if 'integrated_fitCons_score' in row else row['integrated_fit_cons_score']
            annovar_record.integrated_fit_cons_score_rankscore = row['integrated_fitCons_score_rankscore'] if 'integrated_fitCons_score_rankscore' in row else row['integrated_fit_cons_score_rankscore']
            annovar_record.integrated_confidence_value = row['integrated_confidence_value'] if 'integrated_confidence_value' in row else row['integrated_confidence_value']
            annovar_record.gerp_rs = row['GERP.._RS'] if 'GERP.._RS' in row else row['gerp_rs']
            annovar_record.gerp_rs_rankscore = row['GERP.._RS_rankscore'] if 'GERP.._RS_rankscore' in row else row['gerp_rs_rankscore']
            annovar_record.phylo_p_100_way_vertebrate = row['phyloP100way_vertebrate'] if 'phyloP100way_vertebrate' in row else row['phylo_p_100_way_vertebrate']
            annovar_record.phylo_p_100_way_vertebrate_rankscore = row['phyloP100way_vertebrate_rankscore'] if 'phyloP100way_vertebrate_rankscore' in row else row['phylo_p_100_way_vertebrate_rankscore']
            annovar_record.phylo_p_20_way_mammalian = row['phyloP20way_mammalian'] if 'phyloP20way_mammalian' in row else row['phylo_p_20_way_mammalian']
            annovar_record.phylo_p_20_way_mammalian_rankscore = row['phyloP20way_mammalian_rankscore'] if 'phyloP20way_mammalian_rankscore' in row else row['phylo_p_20_way_mammalian_rankscore']
            annovar_record.phast_cons_100_way_vertebrate = row['phastCons100way_vertebrate'] if 'phastCons100way_vertebrate' in row else row['phast_cons_100_way_vertebrate']
            annovar_record.phast_cons_100_way_vertebrate_rankscore = row['phastCons100way_vertebrate_rankscore'] if 'phastCons100way_vertebrate_rankscore' in row else row['phast_cons_100_way_vertebrate_rankscore']
            annovar_record.phast_cons_20_way_mammalian = row['phastCons20way_mammalian'] if 'phastCons20way_mammalian' in row else row['phast_cons_20_way_mammalian']
            annovar_record.phast_cons_20_way_mammalian_rankscore = row['phastCons20way_mammalian_rankscore'] if 'phastCons20way_mammalian_rankscore' in row else row['phast_cons_20_way_mammalian_rankscore']
            annovar_record.si_phy_29_way_log_odds = row['SiPhy_29way_logOdds'] if 'SiPhy_29way_logOdds' in row else row['si_phy_29_way_log_odds']
            annovar_record.si_phy_29_way_log_odds_rankscore = row['SiPhy_29way_logOdds_rankscore'] if 'SiPhy_29way_logOdds_rankscore' in row else row['si_phy_29_way_log_odds_rankscore']
            annovar_record.interpro_domain = row['Interpro_domain'] if 'Interpro_domain' in row else row['interpro_domain']
            annovar_record.gt_ex_v_6_p_gene = row['GTEx_V6p_gene'] if 'GTEx_V6p_gene' in row else row['gt_ex_v_6_p_gene']
            annovar_record.gt_ex_v_6_p_tissue = row['GTEx_V6p_tissue'] if 'GTEx_V6p_tissue' in row else row['gt_ex_v_6_p_tissue']
            annovar_record.cadd_16_gt_10 = row['cadd16gt10'] if 'cadd16gt10' in row else row['cadd_16_gt_10']
            annovar_record.nci_60 = row['nci60'] if 'nci60' in row else row['nci_60']
            annovar_record.clnalleleid = row['CLNALLELEID'] if 'CLNALLELEID' in row else row['clnalleleid']
            annovar_record.clndn = row['CLNDN'] if 'CLNDN' in row else row['clndn']
            annovar_record.clndisdb = row['CLNDISDB'] if 'CLNDISDB' in row else row['clndisdb']
            annovar_record.clnrevstat = row['CLNREVSTAT'] if 'CLNREVSTAT' in row else row['clnrevstat']
            annovar_record.clnsig = row['CLNSIG'] if 'CLNSIG' in row else row['clnsig']
            annovar_record.save()
        else:
            feedback_items.append({'sheet': 'Annovar', 'row_value': chrom_pos, 'issue': "Specified variant does not exist in the system."})
    return feedback_items
