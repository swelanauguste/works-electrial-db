# Generated by Django 5.0.4 on 2024-04-05 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('electrical', '0004_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receipt_no', models.CharField(max_length=10)),
                ('years', models.IntegerField(default=1)),
                ('paid', models.BooleanField(default=False)),
                ('notes', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('electrical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='electrical.electrical')),
            ],
        ),
    ]