# Generated by Django 4.0.3 on 2022-11-08 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_alter_annovardata_func_ref_gene'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annovardata',
            name='avsnp_150',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='cadd_16_gt_10',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='cadd_phred',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='cadd_raw',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='cadd_raw_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='clnalleleid',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='dann_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='dann_score',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='eigen_coding_or_noncoding',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='eigen_pc_raw',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='eigen_raw',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='ex_ac_all',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='exonic_func_ref_gene',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='fathmm_converted_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='fathmm_mkl_coding_pred',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='fathmm_mkl_coding_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='fathmm_mkl_coding_score',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='fathmm_pred',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='fathmm_score',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='gene_ref_gene',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='geno_canyon_score',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='geno_canyon_score_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='gerp_rs',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='gerp_rs_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='gnomad_exome_af_popmax',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='gnomad_genome_af',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='integrated_confidence_value',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='integrated_fit_cons_score',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='integrated_fit_cons_score_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='lrt_converted_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='lrt_pred',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='m_cap_pred',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='m_cap_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='m_cap_score',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='meta_lr_pred',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='meta_lr_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='meta_lr_score',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='meta_svm_pred',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='meta_svm_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='meta_svm_score',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='mut_pred_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='mut_pred_score',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='mutation_assessor_pred',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='mutation_assessor_score_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='mutation_taster_converted_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='mutation_taster_pred',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='nci_60',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='phast_cons_100_way_vertebrate',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='phast_cons_100_way_vertebrate_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='phast_cons_20_way_mammalian',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='phast_cons_20_way_mammalian_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='phylo_p_100_way_vertebrate',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='phylo_p_100_way_vertebrate_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='phylo_p_20_way_mammalian',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='phylo_p_20_way_mammalian_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='polyphen_2_hdiv_pred',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='polyphen_2_hdiv_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='polyphen_2_hdiv_score',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='polyphen_2_hvar_pred',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='polyphen_2_hvar_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='polyphen_2_hvar_score',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='provean_converted_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='provean_pred',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='provean_score',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='revel_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='revel_score',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='si_phy_29_way_log_odds',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='si_phy_29_way_log_odds_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='sift_converted_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='sift_pred',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='vest_3_rankscore',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='annovardata',
            name='vest_3_score',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]