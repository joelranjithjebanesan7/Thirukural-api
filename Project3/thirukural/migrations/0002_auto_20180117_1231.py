# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-17 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thirukural', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thirukural',
            name='ChapterName',
            field=models.CharField(max_length=25),
        ),
    ]
