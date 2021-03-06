# Generated by Django 3.2.6 on 2021-08-20 11:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters allowed')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters allowed')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters allowed')]),
        ),
    ]
