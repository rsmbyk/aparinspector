# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170714_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspectionreport',
            name='waktu_inspeksi',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
