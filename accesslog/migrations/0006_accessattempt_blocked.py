# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-06 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accesslog', '0005_auto_20170202_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessattempt',
            name='blocked',
            field=models.BooleanField(default=False),
        ),
    ]