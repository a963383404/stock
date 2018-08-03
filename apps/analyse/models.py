# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from stockList.models import ShAll, SzAll

class ShAnalyseTotal(models.Model):
    stock = models.ForeignKey(ShAll, verbose_name='代码标识')
    goldTotal = models.IntegerField(default=0, verbose_name='黄金柱个数')
    doubleScaleExpansionTotal = models.IntegerField(default=0, verbose_name='倍量伸缩个数')

    class Meta:
        verbose_name = "上证个股分析统计"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.stock.name

class SzAnalyseTotal(models.Model):
    stock = models.ForeignKey(SzAll, verbose_name='代码标识')
    goldTotal = models.IntegerField(default=0, verbose_name='黄金柱个数')
    doubleScaleExpansionTotal = models.IntegerField(default=0, verbose_name='倍量伸缩个数')

    class Meta:
        verbose_name = "深证个股分析统计"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.stock.name