# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-19 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20190119_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe_info',
            name='recipe_id',
            field=models.IntegerField(unique=True),
        ),
    ]