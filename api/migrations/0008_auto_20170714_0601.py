# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170714_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressurereport',
            name='waktu',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
