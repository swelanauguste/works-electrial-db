# Generated by Django 5.0.4 on 2024-05-15 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0012_rename_bc_inspectionapplication_bc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inspectionapplication',
            old_name='ea',
            new_name='AE',
        ),
        migrations.RenameField(
            model_name='inspectionapplication',
            old_name='en',
            new_name='EN',
        ),
        migrations.RenameField(
            model_name='inspectionapplication',
            old_name='le',
            new_name='LE',
        ),
        migrations.RenameField(
            model_name='inspectionapplication',
            old_name='ln',
            new_name='LN',
        ),
    ]