# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-28 13:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0011_auto_20161120_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='categories',
        ),
    ]
