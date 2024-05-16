# Generated by Django 5.0.4 on 2024-05-15 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0005_alter_inspection_zone'),
    ]

    operations = [
        migrations.CreateModel(
            name='InspectionDailyLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('zone', models.CharField(choices=[('north', 'North'), ('central', 'Central'), ('east/west', 'East/West'), ('special', 'Special')], max_length=100)),
                ('vehicle', models.CharField(choices=[('private', 'Private'), ('SLG', 'SLG')], max_length=8)),
                ('start', models.TimeField()),
                ('location', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=10)),
                ('job_no', models.CharField(max_length=10)),
                ('appl', models.CharField(max_length=5)),
                ('test_data', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('fail', 'Fail'), ('pass', 'Pass')], max_length=4)),
                ('end', models.TimeField()),
                ('assistant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assistants', to='inspections.inspector')),
                ('inspector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inspectors', to='inspections.inspector')),
            ],
        ),
        migrations.DeleteModel(
            name='Inspection',
        ),
    ]