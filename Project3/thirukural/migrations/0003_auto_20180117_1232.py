# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-17 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thirukural', '0002_auto_20180117_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thirukural',
            name='ChapterName',
            field=models.TextField(),
        ),
    ]
