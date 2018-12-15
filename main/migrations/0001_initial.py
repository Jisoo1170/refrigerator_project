# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-06 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('delay', models.IntegerField(default=0)),
                ('site', models.CharField(choices=[('1', '멜론'), ('2', '지니'), ('3', '벅스')], max_length=1)),
                ('reset_list', models.IntegerField(default=0)),
                ('reset_played', models.IntegerField(default=0)),
            ],
        ),
    ]
