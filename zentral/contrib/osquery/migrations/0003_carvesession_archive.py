# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-06 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import zentral.contrib.osquery.models


class Migration(migrations.Migration):

    dependencies = [
        ('osquery', '0002_auto_20170824_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='carvesession',
            name='archive',
            field=models.FileField(null=True, upload_to=zentral.contrib.osquery.models.carve_session_archive_path),
        ),
    ]
