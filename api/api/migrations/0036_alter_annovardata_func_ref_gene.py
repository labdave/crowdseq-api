# Generated by Django 4.0.3 on 2022-11-08 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_annovardata_chrom_pos_ref_alt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annovardata',
            name='func_ref_gene',
            field=models.TextField(),
        ),
    ]