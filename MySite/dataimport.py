import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyWeb.settings")
django.setup()

from MySite.models import GoodsInfo

with open('data', 'r', encoding='utf-8') as file:
    for line in file:
        lst = line.strip().split(',')
        state = GoodsInfo.objects.create(goods_name=lst[0], goods_number=lst[1], goods_price=lst[2])
        print(state)
