# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from stockList.models import ShAll, SzAll, ShAllDetail, SzAllDetail
from analyse.models import ShAnalyseTotal, SzAnalyseTotal

class Command(BaseCommand):
    help = '统计前N个交易日黄金柱总数'

    def add_arguments(self, parser):
        '''
        第一个参数，起始股票，id
        第二个参数，结束股票，id
        第三个参数，统计前N天交易日
        '''
        parser.add_argument('num', nargs='+', type=int)

    def handle(self, *args, **options):
        arg = []
        try:
            for n in options['num']:
                arg.append(int(n))
            if len(arg) != 3:
                raise CommandError('three argments must!')
            self.doubleScaleExpansionTotal(arg)
        except Exception as e:
            print(e)
            raise CommandError('Error')


        self.stdout.write(self.style.SUCCESS('Success.'))

    def doubleScaleExpansionTotal(self, arg):
        a = SzAll.objects.filter(id__lt=arg[1], id__gt=arg[0]).all()
        for s in a:
            d = SzAllDetail.objects.filter(stock=s).order_by('-day').all()[0: arg[2]]

            # 分析是否倍量伸缩
            total = self.isDoubleScaleExpansion(d)

            if total > 0:
                print str(s) + ":" + str(total)
                self.add(s, total)

    def isDoubleScaleExpansion(self, arr):
        total = 0

        l = len(arr)

        i = 1
        while i < l - 2:
            d = arr[i]
            d_pre = arr[i-1]
            d_nex = arr[i+1]

            i = i + 1

            # 条件1，阳柱
            if d.close < d.open:
                continue

            c1 = d.volume > d_pre.volume * 1.8 and d.volume < d_pre.volume * 2.2
            c2 = d.volume > d_nex.volume * 1.8 and d.volume < d_nex.volume * 2.2

            if c1 and c2:
                print str(d.day) + ":" + str(d.close) + " : " + str(d.open) + ",high: " + str(d.high) + "low:" + str(d.low)
                total = total + 1

        return total

    def add(self, obj, total):
        pass