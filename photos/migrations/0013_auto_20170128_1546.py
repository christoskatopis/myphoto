# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-28 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0012_remove_photo_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taggeditem',
            name='content_type',
        ),
        migrations.AddField(
            model_name='photo',
            name='categories',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TaggedItem',
        ),
    ]
