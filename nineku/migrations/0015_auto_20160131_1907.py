# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-31 11:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nineku', '0014_auto_20151225_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dreamdb',
            old_name='dream',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='dreamdb',
            old_name='mood',
            new_name='distance',
        ),
        migrations.RenameField(
            model_name='dreamdb',
            old_name='tags',
            new_name='duration',
        ),
        migrations.AddField(
            model_name='dreamdb',
            name='location',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dreamdb',
            name='time',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dreamdb',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 31, 19, 7, 47, 772296)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 1, 31)),
        ),
    ]
