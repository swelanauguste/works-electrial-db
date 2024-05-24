# Generated by Django 5.0.4 on 2024-05-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inspectionapplication',
            old_name='app_no',
            new_name='job_no',
        ),
        migrations.AlterField(
            model_name='inspectionapplication',
            name='ins_type',
            field=models.CharField(blank=True, choices=[('dom', 'Domestic'), ('com', 'Commercial'), ('temp', 'Temporary'), ('rout', 'Routine'), ('perd', 'Periodic')], max_length=15, null=True, verbose_name='inspection type'),
        ),
        migrations.AlterField(
            model_name='inspectionapplication',
            name='zone',
            field=models.CharField(blank=True, choices=[('north', 'North'), ('central', 'Central'), ('east/west', 'East/West'), ('south', 'South'), ('special', 'Special')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='inspectiondailylog',
            name='zone',
            field=models.CharField(choices=[('north', 'North'), ('central', 'Central'), ('east/west', 'East/West'), ('south', 'South'), ('special', 'Special')], max_length=100),
        ),
    ]
