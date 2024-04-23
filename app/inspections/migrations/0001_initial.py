# Generated by Django 5.0.4 on 2024-04-23 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('electrical', '0005_electrical_created_at_electrical_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('app_no', models.CharField(max_length=5)),
                ('app_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('insp_date', models.DateField()),
                ('description', models.TextField()),
                ('re_insp_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('inspector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wiremen', to='electrical.electrical')),
            ],
        ),
    ]