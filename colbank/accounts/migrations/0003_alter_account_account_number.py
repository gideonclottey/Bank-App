# Generated by Django 3.2.18 on 2023-03-10 23:51

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230310_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.CharField(default=accounts.models.random_string, max_length=10, unique=True),
        ),
    ]