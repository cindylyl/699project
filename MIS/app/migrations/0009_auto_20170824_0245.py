# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-24 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_merge_20170824_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stu_nationality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
