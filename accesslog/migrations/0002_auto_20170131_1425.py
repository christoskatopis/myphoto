# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-31 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accesslog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessattempt',
            name='login_attempts',
            field=models.PositiveIntegerField(default=1),
        ),
    ]