# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-23 08:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20171023_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 23, 8, 53, 47, 881544, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 23, 8, 53, 47, 881544, tzinfo=utc)),
        ),
    ]
