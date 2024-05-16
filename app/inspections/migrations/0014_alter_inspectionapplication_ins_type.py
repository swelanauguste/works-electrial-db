# Generated by Django 5.0.4 on 2024-05-15 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0013_rename_ea_inspectionapplication_ae_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspectionapplication',
            name='ins_type',
            field=models.CharField(blank=True, choices=[('dom', 'Domestic'), ('com', 'Commercial'), ('temp', 'Temporary'), ('rout', 'Routine')], max_length=15, null=True, verbose_name='inspection type'),
        ),
    ]