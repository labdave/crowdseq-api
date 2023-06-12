# Generated by Django 4.0.3 on 2022-07-28 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_ensemblpeptide_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlfaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accession_number', models.TextField()),
                ('accession_number_version', models.TextField()),
                ('chrom', models.TextField()),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('ref', models.TextField()),
                ('alt', models.TextField()),
                ('rsid', models.TextField()),
                ('genbank', models.TextField()),
                ('EUR', models.DecimalField(decimal_places=3, max_digits=6)),
                ('AFO', models.DecimalField(decimal_places=3, max_digits=6)),
                ('EAS', models.DecimalField(decimal_places=3, max_digits=6)),
                ('AFA', models.DecimalField(decimal_places=3, max_digits=6)),
                ('LAC', models.DecimalField(decimal_places=3, max_digits=6)),
                ('LEN', models.DecimalField(decimal_places=3, max_digits=6)),
                ('OAS', models.DecimalField(decimal_places=3, max_digits=6)),
                ('SAS', models.DecimalField(decimal_places=3, max_digits=6)),
                ('OTR', models.DecimalField(decimal_places=3, max_digits=6)),
                ('AFR', models.DecimalField(decimal_places=3, max_digits=6)),
                ('ASN', models.DecimalField(decimal_places=3, max_digits=6)),
                ('TOT', models.DecimalField(decimal_places=3, max_digits=6)),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alfa', to='api.variants')),
            ],
        ),
    ]