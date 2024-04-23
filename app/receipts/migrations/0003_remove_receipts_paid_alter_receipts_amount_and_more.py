# Generated by Django 5.0.4 on 2024-04-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0002_alter_receipts_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipts',
            name='paid',
        ),
        migrations.AlterField(
            model_name='receipts',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=202, max_digits=10),
        ),
        migrations.AlterField(
            model_name='receipts',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]