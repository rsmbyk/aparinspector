# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20170714_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspectionreport',
            name='status',
            field=models.IntegerField(choices=[(-1, 'Ditolak'), (0, 'Menunggu Verifikasi'), (1, 'Terverifikasi')], default=0),
        ),
    ]
