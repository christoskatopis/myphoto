# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-02 18:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accesslog', '0004_auto_20170131_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessattempt',
            name='attempt_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]