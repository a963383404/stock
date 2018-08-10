# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json, os
from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render

from analyse.models import SzAnalyseTotal, ShAnalyseTotal

class HomeView(View):
    def get(self, request):
        return render(request, 'dashboard.html')

    def post(self, request):
        oper = request.POST.get('oper', None)
        msg = {"state": "FAIL", "msg": "收集失败"}

        if oper == 'collectionDoubleScale':
            try:
                v = int(request.POST.get('value', 3))
                self.collectionDoubleScale(v)

                szObj = SzAnalyseTotal.objects.filter(doubleScaleExpansionTotal__gt=0).all()
                shObj = ShAnalyseTotal.objects.filter(doubleScaleExpansionTotal__gt=0).all()

                res = len(szObj) + len(shObj)
                msg['state'] = "SUCCESS"
                msg['msg'] = "收集成功，总共：%s 条。" % res
            except Exception as e:
                pass
        elif oper == 'collectionGold':
            try:
                startId = int(request.POST.get('startId'))
                endId = int(request.POST.get('endId'))
                len = int(request.POST.get('len'))

                self.collectionGold(startId, endId, len)
                msg['state'] = "SUCCESS"
                msg['msg'] = "收集成功：%s到%s" % (startId, endId)
            except Exception as e:
                msg['msg'] = "收集失败：%s到%s" % (startId, endId)
        return HttpResponse(json.dumps(msg, ensure_ascii=False))

    def collectionDoubleScale(self, v):
        c1 = "./manage.py shDoubleScaleExpansionTotal 0 3000 %s" % v
        c2 = "./manage.py szDoubleScaleExpansionTotal 0 3000 %s" % v
        os.system(c1)
        os.system(c2)

    def collectionGold(self, startId, endId, len):
        c1 = './manage.py selectShGlod %s %s %s' % (startId, endId, len)
        c2 = './manage.py selectSzGlod %s %s %s' % (startId, endId, len)
        os.system(c1)
        os.system(c2)