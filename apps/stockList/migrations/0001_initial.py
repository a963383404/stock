# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-03 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShAll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, verbose_name='\u4ee3\u7801')),
                ('name', models.CharField(max_length=100, verbose_name='\u540d\u79f0')),
                ('symbol', models.CharField(max_length=100, verbose_name='\u4ee3\u7801\u6807\u8bc6')),
                ('goldTotal', models.IntegerField(default=0, verbose_name='\u9ec4\u91d1\u67f1\u4e2a\u6570')),
            ],
            options={
                'verbose_name': '\u4e0a\u8bc1\u5217\u8868',
                'verbose_name_plural': '\u4e0a\u8bc1\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='ShAllDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField(verbose_name='\u6210\u4ea4\u91cf')),
                ('high', models.FloatField(verbose_name='\u6700\u9ad8\u4ef7')),
                ('low', models.FloatField(verbose_name='\u6700\u4f4e\u4ef7')),
                ('close', models.FloatField(verbose_name='\u6536\u76d8\u4ef7')),
                ('open', models.FloatField(verbose_name='\u5f00\u76d8\u4ef7')),
                ('day', models.CharField(max_length=100, verbose_name='\u65e5\u671f')),
                ('color', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u989c\u8272')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockList.ShAll', verbose_name='\u4ee3\u7801\u6807\u8bc6')),
            ],
            options={
                'verbose_name': '\u4e0a\u8bc1\u80a1\u7968\u6570\u636e',
                'verbose_name_plural': '\u4e0a\u8bc1\u80a1\u7968\u6570\u636e',
            },
        ),
        migrations.CreateModel(
            name='SzAll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, verbose_name='\u4ee3\u7801')),
                ('name', models.CharField(max_length=100, verbose_name='\u540d\u79f0')),
                ('symbol', models.CharField(max_length=100, verbose_name='\u4ee3\u7801\u6807\u8bc6')),
                ('goldTotal', models.IntegerField(default=0, verbose_name='\u9ec4\u91d1\u67f1\u4e2a\u6570')),
            ],
            options={
                'verbose_name': '\u6df1\u8bc1\u5217\u8868',
                'verbose_name_plural': '\u6df1\u8bc1\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='SzAllDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField(verbose_name='\u6210\u4ea4\u91cf')),
                ('high', models.FloatField(verbose_name='\u6700\u9ad8\u4ef7')),
                ('low', models.FloatField(verbose_name='\u6700\u4f4e\u4ef7')),
                ('close', models.FloatField(verbose_name='\u6536\u76d8\u4ef7')),
                ('open', models.FloatField(verbose_name='\u5f00\u76d8\u4ef7')),
                ('day', models.CharField(max_length=100, verbose_name='\u65e5\u671f')),
                ('color', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u989c\u8272')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockList.SzAll', verbose_name='\u4ee3\u7801\u6807\u8bc6')),
            ],
            options={
                'verbose_name': '\u6df1\u8bc1\u80a1\u7968\u6570\u636e',
                'verbose_name_plural': '\u6df1\u8bc1\u80a1\u7968\u6570\u636e',
            },
        ),
    ]
