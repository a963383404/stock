# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from stockList.models import ShAll, SzAll, ShAllDetail, SzAllDetail

class GoldColumnView(View):
    def get(self, request):
        # 统计最近六十个交易日的黄金数量
        # 改为在命令行中运行
        # self.selectSH()
        # self.selectSZ()

        return HttpResponse(json.dumps('9999'), content_type="application/json")

    def selectSH(self):
        a = ShAll.objects.all()
        for s in a:
            obj = ShAllDetail.objects.filter(stock=s).order_by('-day')[0:60]
            total = 0
            for o in obj:
                if o.color == '#FFD700':
                    total = total + 1
            ShAll.objects.filter(id=s.id).update(goldTotal=total)
            print(str(s.code) + " : " + str(total))

    def selectSZ(self):
        a = SzAll.objects.all()
        for s in a:
            obj = SzAllDetail.objects.filter(stock=s).order_by('-day')[0:60]
            total = 0
            for o in obj:
                if o.color == '#FFD700':
                    total = total + 1
            SzAll.objects.filter(id=s.id).update(goldTotal=total)
            print(str(s.code) + " : " + str(total))

    # 选出含有黄金柱的个股
    @staticmethod
    def filterGoldColumnStock(num=10):
        '''

        选出含有黄金柱的个股
        :param num: 个股最近 num 天中的个股是否含有黄金柱
        :return:
        '''
        pass

class TopGoldView(View):
    def get(self, request):
        shData = ShAll.objects.order_by("-goldTotal").all()[0:10]
        szData = SzAll.objects.order_by("-goldTotal").all()[0:10]
        return render(request, 'topGold.html', {'shData': shData, 'szData': szData})