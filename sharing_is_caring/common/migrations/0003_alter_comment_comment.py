# Generated by Django 3.2.6 on 2021-08-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=200),
        ),
    ]
