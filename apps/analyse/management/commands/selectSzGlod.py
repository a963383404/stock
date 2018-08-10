# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from stockList.models import ShAll, SzAll, ShAllDetail, SzAllDetail

class Command(BaseCommand):
    help = '遍历所有个股日线，黄金柱则为金色，其余为红色或者绿色'

    def add_arguments(self, parser):
        parser.add_argument('num', nargs='+', type=int)

    def handle(self, *args, **options):
        arg = []
        try:
            for n in options['num']:
                arg.append(int(n))
            if len(arg) != 3:
                raise CommandError('three argments must!')
            # 遍历深证个股
            self.selectSZ(arg)
        except Exception as e:
            print(e)
            raise CommandError('Error')


        self.stdout.write(self.style.SUCCESS('Success.'))

    def selectSZ(self, arg):
        a = SzAll.objects.filter(id__lte=arg[1], id__gte=arg[0]).all()
        for s in a:
            d = SzAllDetail.objects.filter(stock=s).order_by('day').all()
            d_l = len(d)
            d_s = d_l - arg[2]
            if d_s < 0:
                d_s = 0
            d = d[d_s:d_l]

            total = 0
            item = []
            for o in d:
                dic = {
                    'id': o.id,
                    'open': o.open,
                    'close': o.close,
                    'volume': o.volume,
                    'day': o.day
                }
                item.append(dic)

            l = len(item)
            i = 0
            while i < l - 3:
                if self.determineGold(item[i], item[i + 1], item[i + 2], item[i + 3]):
                    total = total + 1;
                    # 更新颜色
                    SzAllDetail.objects.filter(id=item[i]['id']).update(color='#FFD700')
                else:
                    if item[i]['close'] > item[i]['open']:
                        # 更新颜色
                        SzAllDetail.objects.filter(id=item[i]['id']).update(color='#FF0000')
                    else:
                        # 更新颜色
                        SzAllDetail.objects.filter(id=item[i]['id']).update(color='#00FF00')
                i = i + 1

            SzAll.objects.filter(id=s.id).update(goldTotal=total)
            print(str(s) + " : " + str(total))

    # 判断是否为黄金柱
    def determineGold(self, a1, a2, a3, a4):
        res = True

        # 条件1，第一天的量柱大于后三天的平均值
        if a1['volume'] < (a2['volume'] + a3['volume'] + a4['volume']) / 3:
            res = False
        # 条件2，第四天的收盘价比第一天高
        if a1['close'] > a4['close']:
            res = False
        # 条件3，当天为阳柱
        if a1['open'] > a1['close']:
            res = False
        return res
