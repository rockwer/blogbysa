# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-07 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20171207_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
