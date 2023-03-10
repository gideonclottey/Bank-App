# Generated by Django 3.2.18 on 2023-03-13 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_account_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user_name',
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default=1, help_text='Enter First Name', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.EmailField(default=1, help_text='Enter Last Name', max_length=254),
            preserve_default=False,
        ),
    ]
