# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View

from stockList.models import SzAll, ShAll

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