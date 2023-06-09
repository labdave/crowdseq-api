# Generated by Django 4.0.3 on 2022-11-10 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_alter_annovardata_avsnp_150_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gnomad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rs_id', models.TextField(blank=True, null=True)),
                ('qual', models.TextField(blank=True, null=True)),
                ('filter', models.TextField(blank=True, null=True)),
                ('gnomad_source_version', models.TextField(blank=True, null=True)),
                ('annotation_type', models.TextField(blank=True, null=True)),
                ('af', models.TextField(blank=True, null=True)),
                ('af_non_neuro_nfe', models.TextField(blank=True, null=True)),
                ('af_non_neuro_nfe_XY', models.TextField(blank=True, null=True)),
                ('af_non_v2', models.TextField(blank=True, null=True)),
                ('af_non_topmed_sas', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_XY', models.TextField(blank=True, null=True)),
                ('af_sas_XY', models.TextField(blank=True, null=True)),
                ('af_non_v2_raw', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_raw', models.TextField(blank=True, null=True)),
                ('af_non_topmed_eas', models.TextField(blank=True, null=True)),
                ('af_non_neuro_sas', models.TextField(blank=True, null=True)),
                ('af_non_cancer_nfe_XY', models.TextField(blank=True, null=True)),
                ('af_non_cancer_XY', models.TextField(blank=True, null=True)),
                ('af_non_v2_sas', models.TextField(blank=True, null=True)),
                ('af_sas', models.TextField(blank=True, null=True)),
                ('af_non_cancer_eas', models.TextField(blank=True, null=True)),
                ('af_non_topmed_XY', models.TextField(blank=True, null=True)),
                ('af_non_neuro', models.TextField(blank=True, null=True)),
                ('af_non_v2_XY', models.TextField(blank=True, null=True)),
                ('af_non_cancer_sas_XY', models.TextField(blank=True, null=True)),
                ('af_non_topmed', models.TextField(blank=True, null=True)),
                ('af_non_cancer_raw', models.TextField(blank=True, null=True)),
                ('af_non_topmed_sas_XY', models.TextField(blank=True, null=True)),
                ('af_non_neuro_eas_XY', models.TextField(blank=True, null=True)),
                ('af_XY', models.TextField(blank=True, null=True)),
                ('af_non_topmed_eas_XY', models.TextField(blank=True, null=True)),
                ('af_eas', models.TextField(blank=True, null=True)),
                ('af_non_cancer_sas', models.TextField(blank=True, null=True)),
                ('af_raw', models.TextField(blank=True, null=True)),
                ('af_eas_XY', models.TextField(blank=True, null=True)),
                ('af_non_v2_nfe_XY', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_sas', models.TextField(blank=True, null=True)),
                ('af_non_cancer_nfe', models.TextField(blank=True, null=True)),
                ('af_non_neuro_sas_XY', models.TextField(blank=True, null=True)),
                ('af_non_topmed_raw', models.TextField(blank=True, null=True)),
                ('af_non_cancer_eas_XY', models.TextField(blank=True, null=True)),
                ('af_non_cancer', models.TextField(blank=True, null=True)),
                ('af_non_v2_sas_XY', models.TextField(blank=True, null=True)),
                ('af_non_neuro_eas', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks', models.TextField(blank=True, null=True)),
                ('af_nfe_XY', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_sas_XY', models.TextField(blank=True, null=True)),
                ('af_non_v2_nfe', models.TextField(blank=True, null=True)),
                ('af_non_neuro_raw', models.TextField(blank=True, null=True)),
                ('af_non_neuro_XY', models.TextField(blank=True, null=True)),
                ('af_nfe', models.TextField(blank=True, null=True)),
                ('af_non_v2_XX', models.TextField(blank=True, null=True)),
                ('af_non_topmed_nfe_XX', models.TextField(blank=True, null=True)),
                ('af_amr_XY', models.TextField(blank=True, null=True)),
                ('af_non_v2_nfe_XX', models.TextField(blank=True, null=True)),
                ('af_non_neuro_XX', models.TextField(blank=True, null=True)),
                ('af_nfe_XX', models.TextField(blank=True, null=True)),
                ('af_non_v2_amr', models.TextField(blank=True, null=True)),
                ('af_non_neuro_nfe_XX', models.TextField(blank=True, null=True)),
                ('af_XX', models.TextField(blank=True, null=True)),
                ('af_non_topmed_nfe', models.TextField(blank=True, null=True)),
                ('af_amr', models.TextField(blank=True, null=True)),
                ('af_non_cancer_nfe_XX', models.TextField(blank=True, null=True)),
                ('af_non_topmed_XX', models.TextField(blank=True, null=True)),
                ('af_non_v2_amr_XY', models.TextField(blank=True, null=True)),
                ('af_non_cancer_amr', models.TextField(blank=True, null=True)),
                ('af_non_neuro_amr_XY', models.TextField(blank=True, null=True)),
                ('af_non_cancer_amr_XY', models.TextField(blank=True, null=True)),
                ('af_non_neuro_amr', models.TextField(blank=True, null=True)),
                ('af_non_cancer_XX', models.TextField(blank=True, null=True)),
                ('af_non_cancer_eas_XX', models.TextField(blank=True, null=True)),
                ('af_non_topmed_amr_XY', models.TextField(blank=True, null=True)),
                ('af_amr_XX', models.TextField(blank=True, null=True)),
                ('af_non_topmed_amr_XX', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_nfe_XX', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_amr_XX', models.TextField(blank=True, null=True)),
                ('af_non_topmed_amr', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_amr', models.TextField(blank=True, null=True)),
                ('af_non_neuro_amr_XX', models.TextField(blank=True, null=True)),
                ('af_non_v2_eas_XX', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_amr_XY', models.TextField(blank=True, null=True)),
                ('af_non_v2_eas', models.TextField(blank=True, null=True)),
                ('af_non_neuro_eas_XX', models.TextField(blank=True, null=True)),
                ('af_non_cancer_amr_XX', models.TextField(blank=True, null=True)),
                ('af_eas_XX', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_nfe', models.TextField(blank=True, null=True)),
                ('af_non_v2_amr_XX', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_XX', models.TextField(blank=True, null=True)),
                ('af_non_v2_eas_XY', models.TextField(blank=True, null=True)),
                ('af_non_neuro_asj_XY', models.TextField(blank=True, null=True)),
                ('af_non_v2_asj', models.TextField(blank=True, null=True)),
                ('af_non_v2_asj_XY', models.TextField(blank=True, null=True)),
                ('af_asj_XY', models.TextField(blank=True, null=True)),
                ('af_non_cancer_asj_XY', models.TextField(blank=True, null=True)),
                ('af_non_topmed_asj', models.TextField(blank=True, null=True)),
                ('af_asj', models.TextField(blank=True, null=True)),
                ('af_non_topmed_asj_XY', models.TextField(blank=True, null=True)),
                ('af_non_neuro_asj', models.TextField(blank=True, null=True)),
                ('af_non_cancer_asj', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_eas', models.TextField(blank=True, null=True)),
                ('af_non_topmed_eas_XX', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_eas_XX', models.TextField(blank=True, null=True)),
                ('af_non_topmed_nfe_XY', models.TextField(blank=True, null=True)),
                ('af_oth', models.TextField(blank=True, null=True)),
                ('af_non_v2_oth', models.TextField(blank=True, null=True)),
                ('af_non_cancer_oth_XY', models.TextField(blank=True, null=True)),
                ('af_non_v2_afr', models.TextField(blank=True, null=True)),
                ('af_non_cancer_afr', models.TextField(blank=True, null=True)),
                ('af_non_v2_oth_XY', models.TextField(blank=True, null=True)),
                ('af_non_v2_afr_XX', models.TextField(blank=True, null=True)),
                ('af_afr', models.TextField(blank=True, null=True)),
                ('af_non_neuro_afr_XX', models.TextField(blank=True, null=True)),
                ('af_oth_XY', models.TextField(blank=True, null=True)),
                ('af_non_neuro_oth', models.TextField(blank=True, null=True)),
                ('af_afr_XX', models.TextField(blank=True, null=True)),
                ('af_non_cancer_afr_XX', models.TextField(blank=True, null=True)),
                ('af_non_cancer_oth', models.TextField(blank=True, null=True)),
                ('af_non_neuro_afr', models.TextField(blank=True, null=True)),
                ('af_non_neuro_oth_XY', models.TextField(blank=True, null=True)),
                ('af_non_cancer_fin_XX', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_eas_XY', models.TextField(blank=True, null=True)),
                ('af_non_neuro_sas_XX', models.TextField(blank=True, null=True)),
                ('af_non_cancer_asj_XX', models.TextField(blank=True, null=True)),
                ('af_fin_XX', models.TextField(blank=True, null=True)),
                ('af_fin', models.TextField(blank=True, null=True)),
                ('af_asj_XX', models.TextField(blank=True, null=True)),
                ('af_sas_XX', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_sas_XX', models.TextField(blank=True, null=True)),
                ('af_non_neuro_asj_XX', models.TextField(blank=True, null=True)),
                ('af_non_v2_sas_XX', models.TextField(blank=True, null=True)),
                ('af_non_topmed_fin', models.TextField(blank=True, null=True)),
                ('af_non_v2_asj_XX', models.TextField(blank=True, null=True)),
                ('af_non_cancer_sas_XX', models.TextField(blank=True, null=True)),
                ('af_non_topmed_fin_XX', models.TextField(blank=True, null=True)),
                ('af_non_topmed_sas_XX', models.TextField(blank=True, null=True)),
                ('af_non_cancer_fin', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_nfe_XY', models.TextField(blank=True, null=True)),
                ('af_non_neuro_afr_XY', models.TextField(blank=True, null=True)),
                ('af_oth_XX', models.TextField(blank=True, null=True)),
                ('af_non_v2_afr_XY', models.TextField(blank=True, null=True)),
                ('af_afr_XY', models.TextField(blank=True, null=True)),
                ('af_non_cancer_oth_XX', models.TextField(blank=True, null=True)),
                ('af_non_neuro_oth_XX', models.TextField(blank=True, null=True)),
                ('af_non_cancer_afr_XY', models.TextField(blank=True, null=True)),
                ('af_non_cancer_fin_XY', models.TextField(blank=True, null=True)),
                ('af_non_topmed_asj_XX', models.TextField(blank=True, null=True)),
                ('af_fin_XY', models.TextField(blank=True, null=True)),
                ('af_non_v2_fin', models.TextField(blank=True, null=True)),
                ('af_non_topmed_fin_XY', models.TextField(blank=True, null=True)),
                ('af_non_v2_fin_XY', models.TextField(blank=True, null=True)),
                ('af_non_neuro_fin', models.TextField(blank=True, null=True)),
                ('af_non_topmed_afr_XX', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_afr', models.TextField(blank=True, null=True)),
                ('af_non_v2_oth_XX', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_afr_XY', models.TextField(blank=True, null=True)),
                ('af_non_neuro_fin_XX', models.TextField(blank=True, null=True)),
                ('af_non_neuro_fin_XY', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_fin', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_afr_XX', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_fin_XX', models.TextField(blank=True, null=True)),
                ('af_non_topmed_afr', models.TextField(blank=True, null=True)),
                ('af_non_topmed_afr_XY', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_oth', models.TextField(blank=True, null=True)),
                ('af_non_topmed_oth', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_oth_XY', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_fin_XY', models.TextField(blank=True, null=True)),
                ('af_non_topmed_oth_XY', models.TextField(blank=True, null=True)),
                ('af_ami', models.TextField(blank=True, null=True)),
                ('af_ami_XY', models.TextField(blank=True, null=True)),
                ('af_non_v2_ami', models.TextField(blank=True, null=True)),
                ('af_non_neuro_ami_XY', models.TextField(blank=True, null=True)),
                ('af_non_cancer_ami', models.TextField(blank=True, null=True)),
                ('af_non_neuro_ami', models.TextField(blank=True, null=True)),
                ('af_non_cancer_ami_XY', models.TextField(blank=True, null=True)),
                ('af_ami_XX', models.TextField(blank=True, null=True)),
                ('af_non_cancer_ami_XX', models.TextField(blank=True, null=True)),
                ('af_non_v2_ami_XX', models.TextField(blank=True, null=True)),
                ('af_non_neuro_ami_XX', models.TextField(blank=True, null=True)),
                ('af_non_v2_ami_XY', models.TextField(blank=True, null=True)),
                ('af_non_v2_mid', models.TextField(blank=True, null=True)),
                ('af_non_topmed_mid_XY', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_ami', models.TextField(blank=True, null=True)),
                ('af_non_topmed_mid', models.TextField(blank=True, null=True)),
                ('af_non_neuro_mid', models.TextField(blank=True, null=True)),
                ('af_mid_XY', models.TextField(blank=True, null=True)),
                ('af_non_cancer_mid', models.TextField(blank=True, null=True)),
                ('af_non_v2_mid_XY', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_mid', models.TextField(blank=True, null=True)),
                ('af_mid', models.TextField(blank=True, null=True)),
                ('af_mid_XX', models.TextField(blank=True, null=True)),
                ('af_non_v2_fin_XX', models.TextField(blank=True, null=True)),
                ('af_non_topmed_ami', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_ami_XY', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_mid_XX', models.TextField(blank=True, null=True)),
                ('af_non_neuro_mid_XY', models.TextField(blank=True, null=True)),
                ('af_non_v2_mid_XX', models.TextField(blank=True, null=True)),
                ('af_non_topmed_mid_XX', models.TextField(blank=True, null=True)),
                ('af_non_topmed_oth_XX', models.TextField(blank=True, null=True)),
                ('af_non_cancer_mid_XX', models.TextField(blank=True, null=True)),
                ('af_non_topmed_ami_XY', models.TextField(blank=True, null=True)),
                ('af_non_neuro_mid_XX', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_oth_XX', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_asj_XX', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_mid_XY', models.TextField(blank=True, null=True)),
                ('af_non_cancer_mid_XY', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_asj_XY', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_asj', models.TextField(blank=True, null=True)),
                ('af_non_topmed_ami_XX', models.TextField(blank=True, null=True)),
                ('af_controls_and_biobanks_ami_XX', models.TextField(blank=True, null=True)),
                ('af_popmax', models.TextField(blank=True, null=True)),
                ('chrom_pos_ref_alt', models.TextField(blank=True, null=True)),
                ('variant', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gnomad', to='api.variants')),
            ],
        ),
        migrations.CreateModel(
            name='CosmicTargetedPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_name', models.TextField()),
                ('accession_number', models.TextField()),
                ('gene_cds_length', models.IntegerField(blank=True, null=True)),
                ('primary_histology', models.TextField(blank=True, null=True)),
                ('histology_subtype_1', models.TextField(blank=True, null=True)),
                ('histology_subtype_2', models.TextField(blank=True, null=True)),
                ('histology_subtype_3', models.TextField(blank=True, null=True)),
                ('primary_site', models.TextField(blank=True, null=True)),
                ('site_subtype_1', models.TextField(blank=True, null=True)),
                ('site_subtype_2', models.TextField(blank=True, null=True)),
                ('site_subtype_3', models.TextField(blank=True, null=True)),
                ('genomic_mutation_id', models.TextField()),
                ('genome_wide_screen', models.BooleanField(default=False)),
                ('legacy_mutation_id', models.TextField(blank=True, null=True)),
                ('mutation_id', models.IntegerField(blank=True, null=True)),
                ('mutation_cds', models.TextField(blank=True, null=True)),
                ('mutation_aa', models.TextField(blank=True, null=True)),
                ('mutation_description', models.TextField(blank=True, null=True)),
                ('mutation_zygosity', models.TextField(blank=True, null=True)),
                ('mutation_genome_position', models.TextField(blank=True, null=True)),
                ('loh', models.TextField(blank=True, null=True)),
                ('mutation_strand', models.TextField(blank=True, null=True)),
                ('resistance_mutation', models.TextField(blank=True, null=True)),
                ('fathmm_prediction', models.TextField(blank=True, null=True)),
                ('fathmm_score', models.DecimalField(blank=True, decimal_places=1, max_digits=7, null=True)),
                ('mutation_somatic_status', models.TextField(blank=True, null=True)),
                ('pubmed_pmid', models.TextField(blank=True, null=True)),
                ('sample_type', models.TextField(blank=True, null=True)),
                ('tumour_origin', models.TextField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('hgvsp_id', models.TextField(blank=True, null=True)),
                ('hgvsc_id', models.TextField(blank=True, null=True)),
                ('hgvsg_id', models.TextField(blank=True, null=True)),
                ('hgnc_id', models.IntegerField(blank=True, null=True)),
                ('gene', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cosmic_targeted', to='api.genes')),
                ('variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cosmic_targeted', to='api.variants')),
            ],
        ),
        migrations.CreateModel(
            name='CosmicResistanceMutation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_name', models.TextField(blank=True, null=True)),
                ('transcript', models.TextField(blank=True, null=True)),
                ('census_gene', models.BooleanField(default=False)),
                ('drug_name', models.TextField(blank=True, null=True)),
                ('histology', models.TextField(blank=True, null=True)),
                ('histology_subtype_1', models.TextField(blank=True, null=True)),
                ('histology_subtype_2', models.TextField(blank=True, null=True)),
                ('zygosity', models.TextField(blank=True, null=True)),
                ('genome_coordinates', models.TextField(blank=True, null=True)),
                ('mutation_id', models.TextField(blank=True, null=True)),
                ('genomic_mutation_id', models.TextField(blank=True, null=True)),
                ('pubmed_pmid', models.TextField(blank=True, null=True)),
                ('sample_type', models.TextField(blank=True, null=True)),
                ('somatic_status', models.TextField(blank=True, null=True)),
                ('primary_tissue', models.TextField(blank=True, null=True)),
                ('tissue_subtype_1', models.TextField(blank=True, null=True)),
                ('tissue_subtype_2', models.TextField(blank=True, null=True)),
                ('legacy_mutation_id', models.TextField(blank=True, null=True)),
                ('aa_mutation', models.TextField(blank=True, null=True)),
                ('cds_mutation', models.TextField(blank=True, null=True)),
                ('tier', models.IntegerField(blank=True, null=True)),
                ('cgp_study', models.TextField(blank=True, null=True)),
                ('hgvsp_id', models.TextField(blank=True, null=True)),
                ('hgvsc_id', models.TextField(blank=True, null=True)),
                ('hgvsg_id', models.TextField(blank=True, null=True)),
                ('variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cosmic_resistance', to='api.variants')),
            ],
        ),
        migrations.CreateModel(
            name='CosmicNonCoding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genomic_mutation_id', models.TextField()),
                ('primary_site', models.TextField(blank=True, null=True)),
                ('site_subtype_1', models.TextField(blank=True, null=True)),
                ('site_subtype_2', models.TextField(blank=True, null=True)),
                ('site_subtype_3', models.TextField(blank=True, null=True)),
                ('primary_histology', models.TextField(blank=True, null=True)),
                ('histology_subtype_1', models.TextField(blank=True, null=True)),
                ('histology_subtype_2', models.TextField(blank=True, null=True)),
                ('histology_subtype_3', models.TextField(blank=True, null=True)),
                ('legacy_mutation_id', models.TextField(blank=True, null=True)),
                ('zygosity', models.TextField(blank=True, null=True)),
                ('genome_position', models.TextField(blank=True, null=True)),
                ('mutation_somatic_status', models.TextField(blank=True, null=True)),
                ('wt_seq', models.TextField(blank=True, null=True)),
                ('mut_seq', models.TextField(blank=True, null=True)),
                ('fathmm_mkl_non_coding_score', models.DecimalField(blank=True, decimal_places=1, max_digits=7, null=True)),
                ('fathmm_mkl_non_coding_group', models.TextField(blank=True, null=True)),
                ('fathmm_mkl_coding_score', models.DecimalField(blank=True, decimal_places=1, max_digits=7, null=True)),
                ('fathmm_mkl_coding_group', models.TextField(blank=True, null=True)),
                ('whole_genome_refseq', models.BooleanField(default=False)),
                ('whole_exome', models.BooleanField(default=False)),
                ('pubmed_pmid', models.TextField(blank=True, null=True)),
                ('hgvsg_id', models.TextField(blank=True, null=True)),
                ('variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cosmic_noncoding', to='api.variants')),
            ],
        ),
        migrations.CreateModel(
            name='CosmicGenomeScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genomic_mutation_id', models.TextField()),
                ('gene_name', models.TextField()),
                ('accession_number', models.TextField()),
                ('gene_cds_length', models.IntegerField(blank=True, null=True)),
                ('primary_site', models.TextField(blank=True, null=True)),
                ('site_subtype_1', models.TextField(blank=True, null=True)),
                ('site_subtype_2', models.TextField(blank=True, null=True)),
                ('site_subtype_3', models.TextField(blank=True, null=True)),
                ('primary_histology', models.TextField(blank=True, null=True)),
                ('histology_subtype_1', models.TextField(blank=True, null=True)),
                ('histology_subtype_2', models.TextField(blank=True, null=True)),
                ('histology_subtype_3', models.TextField(blank=True, null=True)),
                ('genome_wide_screen', models.BooleanField(default=False)),
                ('mutation_id', models.IntegerField(blank=True, null=True)),
                ('mutation_cds', models.TextField(blank=True, null=True)),
                ('mutation_aa', models.TextField(blank=True, null=True)),
                ('mutation_description', models.TextField(blank=True, null=True)),
                ('mutation_zygosity', models.TextField(blank=True, null=True)),
                ('mutation_genome_position', models.TextField(blank=True, null=True)),
                ('loh', models.TextField(blank=True, null=True)),
                ('mutation_strand', models.TextField(blank=True, null=True)),
                ('snp', models.BooleanField(default=False)),
                ('fathmm_prediction', models.TextField(blank=True, null=True)),
                ('fathmm_score', models.DecimalField(blank=True, decimal_places=1, max_digits=7, null=True)),
                ('mutation_somatic_status', models.TextField(blank=True, null=True)),
                ('pubmed_pmid', models.TextField(blank=True, null=True)),
                ('sample_type', models.TextField(blank=True, null=True)),
                ('tumour_origin', models.TextField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('hgvsp_id', models.TextField(blank=True, null=True)),
                ('hgvsc_id', models.TextField(blank=True, null=True)),
                ('hgvsg_id', models.TextField(blank=True, null=True)),
                ('hgnc_id', models.IntegerField(blank=True, null=True)),
                ('gene', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cosmic_genome', to='api.genes')),
                ('variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cosmic_genome', to='api.variants')),
            ],
        ),
    ]
