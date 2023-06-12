"""

"""
import pandas as pd
import json
from django.core.management.base import BaseCommand
from Aries.storage import StorageFile

from api.models import AminoAcidChange, Variants


class Command(BaseCommand):
    """

    See https://docs.djangoproject.com/en/1.11/howto/custom-management-commands/
    """
    help = 'Retrieves missing transcripts for chrom-pos-ref-alt records.'

    def add_arguments(self, parser):
        """Positional arguments

        See https://docs.python.org/3/library/argparse.html for more details about add_argument
        """
        parser.add_argument('file', type=str, help="local excel file with gene and aa change data")

    def handle(self, *args, **options):

        filename = options['file']

        if StorageFile(filename).exists():
            new_file = filename.replace('.xlsx', '_matched.xlsx')
            xls = pd.ExcelFile(filename, engine='openpyxl')
            sheet_1 = xls.sheet_names[0]
            df = pd.read_excel(xls, sheet_name=sheet_1)
            data = df.to_dict('records')
            cpra_list = list(set(row['CHROM_POS_REF_ALT'].replace('chr', '') for row in data))
            aa_list = list(set(str(row['AA_change']) for row in data))
            variant_list = Variants.objects.filter(chrom_pos_ref_alt__in=cpra_list)
            variant_dict = {v.chrom_pos_ref_alt: v for v in variant_list}
            aminoacid_list = AminoAcidChange.objects.filter(short_name__in=aa_list)
            aa_dict = {a.short_name: a for a in aminoacid_list}
            for row in data:
                v_key = row['CHROM_POS_REF_ALT'].replace('chr', '')
                a_key = str(row['AA_change'])
                variant = variant_dict[v_key] if v_key in variant_dict else None
                aa_change = aa_dict[a_key] if a_key in aa_dict else None
                if variant and aa_change:
                    transcript_list = variant.aa_transcript_variants.filter(amino_acid__id=aa_change.id)
                    if transcript_list:
                        for t in transcript_list:
                            if t.transcript.refseq_match:
                                row['transcript'] = t.transcript.refseq_match.split('.')[0]
                            else:
                                refseq_list = t.transcript.refseq_transcripts.all()
                                for r in refseq_list:
                                    row['transcript'] = r.refseq_transcript_id
                                    break
            df = pd.DataFrame(data)
            df.to_excel(new_file, index=False)
