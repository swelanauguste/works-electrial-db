# Generated by Django 5.0.4 on 2024-05-24 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0002_rename_app_no_inspectionapplication_job_no_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inspectionapplication',
            old_name='ins_type',
            new_name='insp_type',
        ),
        migrations.AddField(
            model_name='inspectionapplication',
            name='CT_RT',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='inspectionapplication',
            name='E',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='inspectionapplication',
            name='L1_L2',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='inspectionapplication',
            name='L1_L3',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='inspectionapplication',
            name='L1_L3_L2_E',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='inspectionapplication',
            name='L1_L3_L2_N',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='inspectionapplication',
            name='L3_L2',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='inspectionapplication',
            name='NE',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='inspectionapplication',
            name='RE',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='inspectionapplication',
            name='inst_type',
            field=models.CharField(blank=True, choices=[('1P', '1Phase'), ('3P', '3Phase')], help_text='Installation Phase Type', max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='inspectionapplication',
            name='kW',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='inspectionapplication',
            name='next_inspection',
            field=models.DateField(blank=True, null=True),
        ),
    ]