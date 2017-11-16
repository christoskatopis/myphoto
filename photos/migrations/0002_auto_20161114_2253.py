# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-14 20:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='favorites',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='favorite',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Photo'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]