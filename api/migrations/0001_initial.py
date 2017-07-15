# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 03:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lokasi', models.CharField(max_length=128)),
                ('nomor_lokasi', models.CharField(max_length=8)),
                ('jenis', models.CharField(max_length=8)),
                ('kapasitas', models.IntegerField()),
                ('kadaluarsa', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='InspectionReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu_inspeksi', models.DateField(auto_created=True)),
                ('kondisi', models.BooleanField(choices=[(True, 'Baik'), (False, 'Tidak Baik')])),
                ('catatan', models.TextField(max_length=1024)),
                ('status', models.IntegerField(choices=[(-1, 'Ditolak'), (0, 'Menunggu Verifikasi'), (1, 'Terverifikasi')], default=0)),
                ('apar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Apar')),
                ('inspector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PressureReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu', models.DateTimeField(auto_created=True)),
                ('pembuka', models.CharField(max_length=64)),
                ('penutup', models.CharField(max_length=64)),
                ('t', models.IntegerField()),
                ('p', models.IntegerField()),
                ('b', models.IntegerField()),
                ('nomor', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='qrcode')),
                ('base64', models.CharField(max_length=1024)),
                ('apar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Apar')),
            ],
        ),
        migrations.CreateModel(
            name='VerificationReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu_verifikasi', models.DateTimeField(auto_now_add=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.InspectionReport')),
                ('verificator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='apar',
            name='inspeksi_terakhir',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.VerificationReport'),
        ),
    ]
