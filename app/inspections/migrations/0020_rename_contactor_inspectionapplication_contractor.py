# Generated by Django 5.0.4 on 2024-05-17 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0019_alter_inspectionapplication_ae_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inspectionapplication',
            old_name='contactor',
            new_name='contractor',
        ),
    ]
