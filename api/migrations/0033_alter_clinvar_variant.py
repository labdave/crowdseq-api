# Generated by Django 4.0.3 on 2022-11-07 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_alter_dgidb_gene_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinvar',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clinvar', to='api.variants'),
        ),
    ]