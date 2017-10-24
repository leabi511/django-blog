# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-23 08:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171023_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 23, 8, 30, 4, 795292, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 23, 8, 30, 4, 794791, tzinfo=utc)),
        ),
    ]
