from django.contrib import admin

from .models import Goods


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('goods_name', 'goods_number', 'goods_price')


admin.site.register(Goods, GoodsAdmin)
