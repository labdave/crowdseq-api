# Generated by Django 4.0.3 on 2022-11-09 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_alter_annovardata_clnalleleid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annovardata',
            name='ex_ac_all',
            field=models.TextField(blank=True, null=True),
        ),
    ]
