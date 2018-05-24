# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests, json, time
from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render

from .models import SzAll, ShAll, ShAllDetail, SzAllDetail

class CollectionData(View):
    def get(self, request):
        return render(request, 'collectionData.html')

class CollectionSzList(View):
    API_URL = "http://web.juhe.cn:8080/finance/stock/szall"
    API_KEY = "f2eb7b415a7e9e1c55a94b0983c9db0f"

    # 获取深证股票列表，并存入数据库
    def get(self, request):
        page = 1
        while True:
            url = "%s?key=%s&page=%s" % (self.API_URL, self.API_KEY, page)
            res = requests.get(url)
            res_json = res.json()
            result = res_json['result']
            if result:
                data = result['data']
                for item in data:
                    obj = SzAll.objects.filter(code=item['code'])
                    if not obj:
                        SzAll.objects.create(**{
                            'name': item['name'],
                            'symbol': item['symbol'],
                            'code': item['code'],
                        })
            else:
                break
            page += 1

        msg = {'reason': res_json['reason'], 'error_code': res_json['error_code']}
        return HttpResponse(json.dumps(msg), content_type="application/json")

class CollectionShList(View):
    API_URL = "http://web.juhe.cn:8080/finance/stock/shall"
    API_KEY = "f2eb7b415a7e9e1c55a94b0983c9db0f"

    # 获取深证股票列表，并存入数据库
    def get(self, request):
        page = 1
        while True:
            url = "%s?key=%s&page=%s" % (self.API_URL, self.API_KEY, page)
            res = requests.get(url)
            res_json = res.json()
            result = res_json['result']
            if result:
                data = result['data']
                for item in data:
                    obj = ShAll.objects.filter(code=item['code'])
                    if not obj:
                        ShAll.objects.create(**{
                            'name': item['name'],
                            'symbol': item['symbol'],
                            'code': item['code'],
                        })
            else:
                break
            page += 1

        msg = {'reason': res_json['reason'], 'error_code': res_json['error_code']}
        return HttpResponse(json.dumps(msg), content_type="application/json")

class CollectionDetailData(View):
    URL = "http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol=%s&scale=60&ma=no&datalen=1023"
    result = {'market': None,  'state': 'SUCCESS', 'id': None}

    def get(self, request):
        market = request.GET.get("market", None)
        id = request.GET.get("id", 0)

        print request.GET
        # 解决ConnectionError
        try:
            if market != 'SH':
                # 处理深证数据
                self.handleSzData(int(id))

            if market == 'SZ':
                id = 0

            # 处理上证数据
            self.handleShData(int(id))
        except requests.exceptions.ConnectionError as e:
            self.result['state'] = 'FAIL'
        except Exception as e:
            self.result = {'market': market, 'state': 'FAIL', 'id': id}

        return HttpResponse(json.dumps(self.result), content_type="application/json")

    # 处理深证数据
    def handleSzData(self, id):
        allObj = SzAll.objects.filter(id__gt=id).all()

        for szObj in allObj:
            data = self.changeDate(szObj.symbol)
            for data_item in data:
                res = self.saveSzData(data_item, szObj)
                if not res:
                    break

    # 将数据存入数据库中
    def saveSzData(self, data, obj):
        o = SzAllDetail.objects.filter(stock=obj, day=data['day'])
        if o:
            o = o.get()
            print "%s--SZ_ID:%s" % (o.day, o.stock.id)
            self.result = {'market': 'SZ', 'state': 'SUCCESS', 'id': o.stock.id}
            return False
        else:
            SzAllDetail.objects.create(**{
                'volume': data['volume'],
                'close': data['close'],
                'low': data['low'],
                'high': data['high'],
                'open': data['open'],
                'day': data['day'],
                'stock': obj,
            })
            return True

    # 处理上证数据
    def handleShData(self, id):
        allObj = ShAll.objects.filter(id__gt=id).all()

        for shObj in allObj:
            data = self.changeDate(shObj.symbol)
            for data_item in data:
                res = self.saveShData(data_item, shObj)
                if not res:
                    break

    # 将数据存入数据库中
    def saveShData(self, data, obj):
        o = ShAllDetail.objects.filter(stock__code=obj.code, day=data['day'])
        if o:
            o = o.get()
            print "%s--SH_ID:%s" % (o.day, o.stock.id)
            self.result = {'market': 'SH', 'state': 'SUCCESS', 'id': o.stock.id}
            return False
        else:
            ShAllDetail.objects.create(**{
                'volume': data['volume'],
                'close': data['close'],
                'low': data['low'],
                'high': data['high'],
                'open': data['open'],
                'day': data['day'],
                'stock': obj,
            })
            return True

    # 处理数据
    def changeDate(self, symbol):
        url = self.URL % symbol
        res = requests.get(url)
        # res_json = res.json()
        res_text = res.text
        re = ['day', 'open', 'high', 'low', 'close', 'volume']
        for ch in re:
            res_text = res_text.replace(ch, '"%s"' % ch)

        res_json = json.loads(res_text)
        res_json = res_json[::-1]

        i = 0
        newData = []
        for item in res_json:
            volume = int(item['volume'])
            high = float(item['high'])
            low = float(item['low'])
            close = float(item['close'])
            open = float(item['open'])
            day = item['day']

            if i == 0:
                d = {
                    'volume': volume,
                    'high': high,
                    'low': low,
                    'close': close,
                    'open': open,
                    'day': day.split(" ")[0]
                }
            else:
                d['volume'] += volume
                d['high'] = high if high > d['high'] else d['high']
                d['low'] = low if low < d['low'] else d['low']
                d['close'] = close
                d['open'] = open

            i += 1
            if i > 3:
                newData.append(d)
                d = {}
                i = 0

        return newData