# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20170714_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inspectionreport',
            name='status',
        ),
        migrations.AddField(
            model_name='verificationreport',
            name='status',
            field=models.IntegerField(choices=[(0, 'Ditolak'), (1, 'Terverifikasi')], default=0),
            preserve_default=False,
        ),
    ]
