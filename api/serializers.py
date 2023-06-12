import logging

from rest_framework import serializers
from api import models

# Get an instance of a logger
logger = logging.getLogger(__name__)


class GeneAnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GeneAnnotation
        fields = serializers.ALL_FIELDS


class ScoredGeneAnnotationSerializer(serializers.ModelSerializer):

    # Create a custom method field
    score = serializers.SerializerMethodField('_score')

    # Use this method for the custom field
    def _score(self, obj):
        request = self.context.get('request', None)
        if request and obj.user:
            score = obj.priority
            if obj.user and obj.user.affiliation_id_id == request.user.affiliation_id_id:
                score += 100
            if obj.user and obj.user == request.user:
                score += 1000
            return score
        else:
            return obj.priority

    class Meta:
        model = models.GeneAnnotation
        fields = serializers.ALL_FIELDS


class GeneWithAnnotationSerializer(serializers.ModelSerializer):
    annotations = ScoredGeneAnnotationSerializer(many=True, required=False)

    class Meta:
        model = models.Genes
        fields = serializers.ALL_FIELDS


class GeneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genes
        fields = serializers.ALL_FIELDS


class GeneSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genes
        fields = serializers.ALL_FIELDS


class TranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transcript
        fields = serializers.ALL_FIELDS


class TranscriptNoAASerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transcript
        exclude = ('aa_changes',)


class PublicAnnovarSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AnnovarData
        exclude = ('id', 'variant', 'chrom_pos_ref_alt', )

class PublicClinvarSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Clinvar
        exclude = ('id', 'variant', 'chrom_pos_ref_alt', )


class AminoAcidChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AminoAcidChange
        exclude = ('transcript', 'genes',)


class AminoAcidSearchSerializer(serializers.ModelSerializer):
    genes = GeneSerializer(many=True, required=False)

    class Meta:
        model = models.AminoAcidChange
        exclude = ('transcript',)


class AminoAcidAnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AminoAcidAnnotations
        fields = serializers.ALL_FIELDS


class ScoredAminoAcidAnnotationSerializer(serializers.ModelSerializer):

    # Create a custom method field
    score = serializers.SerializerMethodField('_score')

    # Use this method for the custom field
    def _score(self, obj):
        request = self.context.get('request', None)
        if request and obj.user:
            score = obj.priority
            if obj.user and obj.user.affiliation_id_id == request.user.affiliation_id_id:
                score += 100
            if obj.user and obj.user == request.user:
                score += 1000
            return score
        else:
            return obj.priority

    class Meta:
        model = models.AminoAcidAnnotations
        fields = serializers.ALL_FIELDS


class GeneAminoAcidSerializer(serializers.ModelSerializer):
    genes = GeneSerializer(many=True, required=False)
    annotations = ScoredAminoAcidAnnotationSerializer(many=True, required=False)

    class Meta:
        model = models.AminoAcidChange
        exclude = ('transcript',)


class MappingAminoAcidSerializer(serializers.ModelSerializer):
    amino_acid = AminoAcidChangeSerializer(many=False, required=False)

    class Meta:
        model = models.AminoAcidTranscriptVariant
        exclude = ('transcript', 'variant',)


class TranscriptAminoAcidSerializer(serializers.ModelSerializer):
    amino_acid_changes = GeneAminoAcidSerializer(many=True, required=False)

    class Meta:
        model = models.Transcript
        exclude = ('id',)


class MappingTranscriptSerializer(serializers.ModelSerializer):
    transcript = TranscriptAminoAcidSerializer(many=False, required=False)

    class Meta:
        model = models.AminoAcidTranscriptVariant
        exclude = ('amino_acid', 'variant',)


class VariantSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Variants
        exclude = ('transcripts', 'amino_acid_changes',)


class VariantGeneSerializer(serializers.ModelSerializer):
    gene = GeneSearchSerializer(many=False, required=False)

    class Meta:
        model = models.Variants
        fields = serializers.ALL_FIELDS


class MappingVariantSerializer(serializers.ModelSerializer):
    variant = VariantSearchSerializer(many=False, required=False)

    class Meta:
        model = models.AminoAcidTranscriptVariant
        exclude = ('transcript', 'amino_acid',)


class AminoAcidWithAnnotationsSerializer(serializers.ModelSerializer):
    annotations = ScoredAminoAcidAnnotationSerializer(many=True, required=False)
    genes = GeneWithAnnotationSerializer(many=True, required=False)
    transcript = TranscriptSerializer(many=True, required=False)
    variants = VariantGeneSerializer(many=True, required=False)

    class Meta:
        model = models.AminoAcidChange
        fields = serializers.ALL_FIELDS


class AminoAcidTranscriptSerializer(serializers.ModelSerializer):
    annotations = ScoredAminoAcidAnnotationSerializer(many=True, required=False)
    transcript = TranscriptSerializer(many=True, required=False)
    genes = GeneSerializer(many=True, required=False)

    class Meta:
        model = models.AminoAcidChange
        fields = serializers.ALL_FIELDS


class VariantSerializer(serializers.ModelSerializer):
    aa_transcript_variants = MappingAminoAcidSerializer(many=True, required=False)
    gene = GeneWithAnnotationSerializer(many=False, required=False)

    class Meta:
        model = models.Variants
        fields = serializers.ALL_FIELDS


class VariantAminoAcidSerializer(serializers.ModelSerializer):
    aa_transcript_variants = MappingAminoAcidSerializer(many=True, required=False)
    gene = GeneWithAnnotationSerializer(many=False, required=False)

    class Meta:
        model = models.Variants
        exclude = ('transcripts', 'amino_acid_changes',)


class VariantTranscriptSerializer(serializers.ModelSerializer):
    amino_acid_changes = AminoAcidTranscriptSerializer(many=True, required=False)
    gene = GeneWithAnnotationSerializer(many=False, required=False)
    annovar = PublicAnnovarSerializer(many=True, required=False)
    clinvar = PublicClinvarSerializer(many=True, required=False)

    class Meta:
        model = models.Variants
        exclude = ('transcripts',)


class GeneVariantAminoAcidSerializer(serializers.ModelSerializer):
    aa_transcript_variants = MappingAminoAcidSerializer(many=True, required=False)

    class Meta:
        model = models.Variants
        exclude = ('transcripts', 'amino_acid_changes',)


class SearchSerializer(serializers.Serializer):
    variants = VariantSearchSerializer(source='search_variants', many=True, required=False)
    genes = GeneSearchSerializer(source='search_genes', many=True, required=False)
    aa_changes = AminoAcidSearchSerializer(source='search_aa_changes', many=True, required=False)


class FullAminoAcidSerializer(serializers.ModelSerializer):
    transcripts = TranscriptNoAASerializer(many=True, required=False)
    annotations = ScoredAminoAcidAnnotationSerializer(many=True, required=False)

    class Meta:
        model = models.AminoAcidChange
        fields = serializers.ALL_FIELDS


class FullGeneSerializer(serializers.ModelSerializer):
    variants = GeneVariantAminoAcidSerializer(many=True, required=False)
    annotations = GeneAnnotationSerializer(many=True, required=False)

    class Meta:
        model = models.Genes
        fields = serializers.ALL_FIELDS


class AlfaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AlfaData
        exclude = ('id',)
