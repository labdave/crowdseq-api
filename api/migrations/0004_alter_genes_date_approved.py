# Generated by Django 4.0.3 on 2022-04-02 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_genes_ensembl_gene_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genes',
            name='date_approved',
            field=models.DateField(blank=True, null=True),
        ),
    ]