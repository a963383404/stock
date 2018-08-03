# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from stockList.models import ShAll, SzAll, ShAllDetail, SzAllDetail
from analyse.models import ShAnalyseTotal, SzAnalyseTotal

class Command(BaseCommand):
    help = '统计前N个交易日黄金柱总数'

    def add_arguments(self, parser):
        parser.add_argument('num', nargs='+', type=int)

    def handle(self, *args, **options):
        arg = []
        try:
            for n in options['num']:
                arg.append(int(n))
            if len(arg) != 1:
                raise CommandError('two argments must!')
            self.changeTotalGlod(arg)
        except Exception as e:
            print e
            raise CommandError('Error')


        self.stdout.write(self.style.SUCCESS('Success.'))

    def changeTotalGlod(self, arg):
        self.selectSH(arg)
        self.selectSZ(arg)

    def selectSH(self, arg):
        a = ShAll.objects.all()
        for s in a:
            obj = ShAllDetail.objects.filter(stock=s).order_by('-day')[0 : arg[0]]
            total = 0
            for o in obj:
                if o.color == '#FFD700':
                    total = total + 1
            ShAll.objects.filter(id=s.id).update(goldTotal=total)
            # 添加到 ShAnalyseTotal 中
            self.addShAnalyseTotal(s, total)
            print str(s.code) + " : " + str(total)

    def selectSZ(self, arg):
        a = SzAll.objects.all()
        for s in a:
            obj = SzAllDetail.objects.filter(stock=s).order_by('-day')[0 : arg[0]]
            total = 0
            for o in obj:
                if o.color == '#FFD700':
                    total = total + 1
            SzAll.objects.filter(id=s.id).update(goldTotal=total)
            # 添加到SzAnalyse
            self.addSzAnalyseTotal(s, total)
            print str(s.code) + " : " + str(total)

    def addShAnalyseTotal(self, stock, goldTotal):
        obj = ShAnalyseTotal.objects.filter(stock=stock)
        if obj:
            obj.update(goldTotal=goldTotal)
        else:
            ShAnalyseTotal.objects.create(goldTotal=goldTotal, stock=stock)

    def addSzAnalyseTotal(self, stock, goldTotal):
        obj = SzAnalyseTotal.objects.filter(stock=stock)
        if obj:
            obj.update(goldTotal=goldTotal)
        else:
            SzAnalyseTotal.objects.create(goldTotal=goldTotal, stock=stock)