# Generated by Django 5.0.4 on 2024-05-13 21:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inspector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('log_sheet', models.FileField(blank=True, null=True, upload_to='inspections/log_sheets/')),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('zone', models.CharField(max_length=100)),
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
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet_no', models.IntegerField(null=True, unique=True)),
                ('date', models.DateField()),
                ('app_no', models.CharField(max_length=5, verbose_name='application number')),
                ('app_name', models.CharField(max_length=100, verbose_name="applicant's name")),
                ('location', models.CharField(max_length=255)),
                ('insp_date', models.DateField(verbose_name='inspection date')),
                ('defects', models.TextField()),
                ('re_insp_fee', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='re-inspection fee')),
                ('defect_sheet', models.FileField(null=True, upload_to='inspections/defect_sheet/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('inspector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wiremen', to='inspections.inspector')),
            ],
        ),
        migrations.AddField(
            model_name='inspector',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offices', to='inspections.location'),
        ),
        migrations.AddField(
            model_name='inspector',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='inspections.post'),
        ),
    ]
