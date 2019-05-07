from django.db import models


class Goods(models.Model):
    # 商品名称
    goods_name = models.CharField(max_length=30)
    # 商品数量
    goods_number = models.IntegerField()
    # 商品价格
    goods_price = models.FloatField()
