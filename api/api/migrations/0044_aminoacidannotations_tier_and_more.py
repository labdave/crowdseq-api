# Generated by Django 4.0.3 on 2022-11-30 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0043_aminoacidannotations_ds_id_geneannotation_ds_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='aminoacidannotations',
            name='tier',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aminoacidannotations',
            name='tier_summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]