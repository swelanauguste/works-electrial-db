# Generated by Django 5.0.4 on 2024-04-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0003_rename_description_inspection_defects'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection',
            name='defect_sheet',
            field=models.FileField(null=True, upload_to='inspections/defect_sheet/'),
        ),
    ]
