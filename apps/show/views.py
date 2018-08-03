# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from django.shortcuts import render
from django.views.generic.base import View

from stockList.models import SzAll, ShAll, SzAllDetail, ShAllDetail

class HighStock(View):
    def get(self, request):
        stock = request.GET.get("stock", None)

        result = {'state': 'fail', 'data': {}}
        try:
            obj = SzAll.objects.filter(code=stock)
            if not obj:
                obj = ShAll.objects.filter(code=stock)
            if obj:
                result['state'] = 'success'
                result['data'] = obj.get()
        except Exception:
            pass
        return render(request, 'hightStock.html', {'result': result})

class CustomStock(View):
    def get(self, request):
        '''
        data的格式为：
        [
            {
                'timeStamp': '时间戳',
                'open': '开盘价',
                'high': '最高价',
                'low': '最低价',
                'close': '收盘价',
                'color': '颜色',
                'lineColor': '颜色',
            },
            ...
        ]
        '''
        code = 300234
        data = self.getData(code)

        return render(request, 'customStock.html', {'data': data})

    # 生成 HightStock 对就的数据格式
    def getData(self, code):
        data = []

        try:
            stock = SzAll.objects.filter(code=code).get()
            obj = SzAllDetail.objects.filter(stock=stock).order_by('day').all()
            for o in obj:
                open = float(o.open)
                close = float(o.close)
                day = "%s 00:00:00" % o.day
                day = time.mktime(time.strptime(day, '%Y-%m-%d %H:%M:%S')) * 1000

                color = 'green'
                if close > open:
                    color = 'red'
                if o.color:
                    color = o.color

                data.append({
                    'timeStamp': day,
                    'open': o.open,
                    'high': o.high,
                    'low': o.low,
                    'close': o.close,
                    'volume': o.volume,
                    'color': color,
                    'lineColor':  color,
                    'stock': o.stock.name
                })
        except Exception:
            pass

        return data

class ShStock(View):
    def get(self, request):
        '''
        data的格式为：
        [
            {
                'timeStamp': '时间戳',
                'open': '开盘价',
                'high': '最高价',
                'low': '最低价',
                'close': '收盘价',
                'color': '颜色',
                'lineColor': '颜色',
            },
            ...
        ]
        '''
        code = request.GET.get('code', 600012)
        data = self.getData(code)
        return render(request, 'customStock.html', {'data': data})

    # 生成 HightStock 对就的数据格式
    def getData(self, code):
        data = []

        try:
            stock = ShAll.objects.filter(code=code).get()
            obj = ShAllDetail.objects.filter(stock=stock).order_by('day').all()
            for o in obj:
                open = float(o.open)
                close = float(o.close)
                day = "%s 00:00:00" % o.day
                day = time.mktime(time.strptime(day, '%Y-%m-%d %H:%M:%S')) * 1000

                color = 'green'
                if close > open:
                    color = 'red'
                if o.color:
                    color = o.color

                data.append({
                    'timeStamp': day,
                    'open': o.open,
                    'high': o.high,
                    'low': o.low,
                    'close': o.close,
                    'volume': o.volume,
                    'color': color,
                    'lineColor':  color,
                    'stock': o.stock.name
                })
        except Exception:
            pass

        return data

class SzStock(View):
    def get(self, request):
        '''
        data的格式为：
        [
            {
                'timeStamp': '时间戳',
                'open': '开盘价',
                'high': '最高价',
                'low': '最低价',
                'close': '收盘价',
                'color': '颜色',
                'lineColor': '颜色',
            },
            ...
        ]
        '''
        code = request.GET.get('code', 300001)
        data = self.getData(code)

        return render(request, 'customStock.html', {'data': data})

    # 生成 HightStock 对就的数据格式
    def getData(self, code):
        data = []

        try:
            stock = SzAll.objects.filter(code=code).get()
            obj = SzAllDetail.objects.filter(stock=stock).order_by('day').all()
            for o in obj:
                open = float(o.open)
                close = float(o.close)
                day = "%s 00:00:00" % o.day
                day = time.mktime(time.strptime(day, '%Y-%m-%d %H:%M:%S')) * 1000

                color = 'green'
                if close > open:
                    color = 'red'
                if o.color:
                    color = o.color

                data.append({
                    'timeStamp': day,
                    'open': o.open,
                    'high': o.high,
                    'low': o.low,
                    'close': o.close,
                    'volume': o.volume,
                    'color': color,
                    'lineColor':  color,
                    'stock': o.stock.name
                })
        except Exception:
            pass

        return data