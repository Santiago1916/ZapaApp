# Generated by Django 3.2.5 on 2022-05-16 01:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20220516_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canal',
            name='usuarios',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), null=True, size=None),
        ),
    ]