from django.db import models


# 创建商品信息的数据模型
class Goods(models.Model):
    # 商品名称
    goods_name = models.CharField(max_length=30)
    # 商品数量
    goods_number = models.IntegerField()
    # 商品价格
    goods_price = models.FloatField()


# 创建用户信息的数据模型
class Users(models.Model):
    # 用户名
    username = models.CharField(max_length=20, primary_key=True)
    # 密码
    password = models.CharField(max_length=20)


# 创建商品信息模型
class GoodsInfo(models.Model):
    # 商品名称
    goods_name = models.CharField(max_length=30, primary_key=True)
    # 商品数量
    goods_number = models.IntegerField()
    # 商品价格
    goods_price = models.FloatField()
