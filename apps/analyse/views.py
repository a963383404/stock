# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from stockList.models import ShAll, SzAll, ShAllDetail, SzAllDetail

class GoldColumnView(View):
    def get(self, request):
        self.selectSH()
        return HttpResponse(json.dumps('9999'), content_type="application/json")

    def selectSH(self):
        a = ShAll.objects.all()
        for s in a:
            obj = ShAllDetail.objects.filter(stock=s).order_by('day').all()
            for o in obj:
                print o.open

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