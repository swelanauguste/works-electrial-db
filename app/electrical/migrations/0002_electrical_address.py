# Generated by Django 5.0.4 on 2024-04-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrical', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='electrical',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]