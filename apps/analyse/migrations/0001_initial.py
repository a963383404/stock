# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-03 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stockList', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShAnalyseTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goldTotal', models.IntegerField(default=0, verbose_name='\u9ec4\u91d1\u67f1\u4e2a\u6570')),
                ('doubleScaleExpansionTotal', models.IntegerField(default=0, verbose_name='\u500d\u91cf\u4f38\u7f29\u4e2a\u6570')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockList.ShAll', verbose_name='\u4ee3\u7801\u6807\u8bc6')),
            ],
            options={
                'verbose_name': '\u4e0a\u8bc1\u4e2a\u80a1\u5206\u6790\u7edf\u8ba1',
                'verbose_name_plural': '\u4e0a\u8bc1\u4e2a\u80a1\u5206\u6790\u7edf\u8ba1',
            },
        ),
        migrations.CreateModel(
            name='SzAnalyseTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goldTotal', models.IntegerField(default=0, verbose_name='\u9ec4\u91d1\u67f1\u4e2a\u6570')),
                ('doubleScaleExpansionTotal', models.IntegerField(default=0, verbose_name='\u500d\u91cf\u4f38\u7f29\u4e2a\u6570')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockList.SzAll', verbose_name='\u4ee3\u7801\u6807\u8bc6')),
            ],
            options={
                'verbose_name': '\u6df1\u8bc1\u4e2a\u80a1\u5206\u6790\u7edf\u8ba1',
                'verbose_name_plural': '\u6df1\u8bc1\u4e2a\u80a1\u5206\u6790\u7edf\u8ba1',
            },
        ),
    ]
