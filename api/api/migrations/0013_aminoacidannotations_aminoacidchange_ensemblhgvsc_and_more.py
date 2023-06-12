# Generated by Django 4.0.3 on 2022-06-02 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0012_diagnosiscategory_geneannotation_diagnosis_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AminoAcidAnnotations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annotation', models.TextField()),
                ('priority', models.IntegerField()),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True, db_column='creation_timestamp')),
            ],
        ),
        migrations.CreateModel(
            name='AminoAcidChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_name', models.TextField(unique=True)),
                ('short_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EnsemblHGVSC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hgvsc_id', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnsemblPeptide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hgvsp_id', models.TextField(unique=True)),
                ('peptide_id', models.TextField(blank=True, null=True)),
                ('canonical', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LRGHGVSC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hgvsc_id', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LRGPeptide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hgvsp_id', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LRGTranscript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lrg_transcript_id', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RefSeqHGVSC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hgvsc_id', models.TextField()),
                ('transcript_type', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RefSeqPeptide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peptide_id', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RefSeqTranscript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refseq_transcript_id', models.TextField(unique=True)),
                ('transcript_type', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ensembl_transcript_id', models.TextField(unique=True)),
                ('transcript_support_level', models.TextField(blank=True, null=True)),
                ('transcript_length', models.IntegerField(blank=True, null=True)),
                ('reqseq_match', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AminoAcidAnnotation',
        ),
        migrations.AddField(
            model_name='refseqtranscript',
            name='transcript',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refseq_transcripts', to='api.transcript'),
        ),
        migrations.AddField(
            model_name='refseqpeptide',
            name='transcript',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peptides', to='api.refseqtranscript'),
        ),
        migrations.AddField(
            model_name='refseqhgvsc',
            name='transcript',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hgvsc', to='api.refseqtranscript'),
        ),
        migrations.AddField(
            model_name='lrgtranscript',
            name='transcript',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lrg_transcripts', to='api.transcript'),
        ),
        migrations.AddField(
            model_name='lrgpeptide',
            name='transcript',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peptides', to='api.lrgtranscript'),
        ),
        migrations.AddField(
            model_name='lrghgvsc',
            name='transcript',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hgvsc', to='api.lrgtranscript'),
        ),
        migrations.AddField(
            model_name='ensemblpeptide',
            name='transcript',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peptides', to='api.transcript'),
        ),
        migrations.AddField(
            model_name='ensemblhgvsc',
            name='transcript',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hgvsc', to='api.transcript'),
        ),
        migrations.AddField(
            model_name='aminoacidchange',
            name='transcripts',
            field=models.ManyToManyField(related_name='aa_changes', to='api.transcript'),
        ),
        migrations.AddField(
            model_name='aminoacidannotations',
            name='amino_acid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to='api.aminoacidchange'),
        ),
        migrations.AddField(
            model_name='aminoacidannotations',
            name='diagnosis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aachange_annotations', to='api.diagnosiscategory'),
        ),
        migrations.AddField(
            model_name='aminoacidannotations',
            name='user',
            field=models.ForeignKey(blank=True, db_column='user', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='variants',
            name='transcripts',
            field=models.ManyToManyField(related_name='variants', to='api.transcript'),
        ),
    ]