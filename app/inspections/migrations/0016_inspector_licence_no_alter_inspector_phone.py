# Generated by Django 5.0.4 on 2024-05-15 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0015_alter_inspectionapplication_ma'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspector',
            name='licence_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspector',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]