# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class SzAll(models.Model):
    code = models.CharField(max_length=100, blank=False, null=False, verbose_name='代码')
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='名称')
    symbol = models.CharField(max_length=100, blank=False, null=False, verbose_name='代码标识')

    class Meta:
        verbose_name = "深证列表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.code

class ShAll(models.Model):
    code = models.CharField(max_length=100, blank=False, null=False, verbose_name='代码')
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='名称')
    symbol = models.CharField(max_length=100, blank=False, null=False, verbose_name='代码标识')

    class Meta:
        verbose_name = "上证列表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.code

class SzAllDetail(models.Model):
    volume = models.IntegerField(blank=False, null=False, verbose_name='成交量')
    high = models.FloatField(blank=False, null=False, verbose_name='最高价')
    low = models.FloatField(blank=False, null=False, verbose_name='最低价')
    close = models.FloatField(blank=False, null=False, verbose_name='收盘价')
    open = models.FloatField(blank=False, null=False, verbose_name='开盘价')
    day = models.CharField(blank=False, null=False, verbose_name='日期', max_length=100)
    stock = models.ForeignKey(SzAll, verbose_name='代码标识')

    class Meta:
        verbose_name = "深证股票数据"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.stock

class ShAllDetail(models.Model):
    volume = models.IntegerField(blank=False, null=False, verbose_name='成交量')
    high = models.FloatField(blank=False, null=False, verbose_name='最高价')
    low = models.FloatField(blank=False, null=False, verbose_name='最低价')
    close = models.FloatField(blank=False, null=False, verbose_name='收盘价')
    open = models.FloatField(blank=False, null=False, verbose_name='开盘价')
    day = models.CharField(blank=False, null=False, verbose_name='日期', max_length=100)
    stock = models.ForeignKey(ShAll, verbose_name='代码标识')

    class Meta:
        verbose_name = "上证股票数据"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.stock