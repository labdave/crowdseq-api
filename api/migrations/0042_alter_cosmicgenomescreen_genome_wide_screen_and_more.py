# Generated by Django 4.0.3 on 2022-11-17 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_gnomad_cosmictargetedpanel_cosmicresistancemutation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cosmicgenomescreen',
            name='genome_wide_screen',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cosmicgenomescreen',
            name='snp',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
