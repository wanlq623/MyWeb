from django.shortcuts import render
# 从http模块中导入HttpResponse类
from django.http import HttpResponse
from MyWeb import trans
from .models import Goods
from django.db.models import Q


# 定义站点首页视图函数
def index(request):
    # 返回响应内容对象
    return render(request, 'index.html')


# 定义翻译视图函数
def translate(request):
    from_lang = request.GET['from_lang']
    to_lang = request.GET['to_lang']
    text = request.GET['words']
    return HttpResponse(trans.trans(text, from_lang, to_lang))


# 定义翻译2视图函数
def translate2(request, words, from_lang, to_lang):
    return HttpResponse(trans.trans(words, from_lang, to_lang))


# 定义新闻列表视图
def news_list(request, news_type):
    # 创建参数字典
    news_dict = {'economic': '经济', 'sport': '体育'}
    news_titles = []
    if news_type == 'economic':
        news_titles = [('12/5', '作者成为全国首富。'), ('12/4', '作者成为全省首富。'),
                       ('12/3', '作者成为全市首富。'), ('12/2', '作者成为镇里首富。'), ('12/1', '作者成为村里首富。')]
    # 整合数据并返回页面内容
    return render(request, 'news_list.html', {'news_type': news_dict[news_type], 'news_titles': news_titles})


# 定义过滤器测试视图
def fiter_test(request):
    return render(request, 'filter.html', {'letters': 'abc', 'number': 1})


# 定义查询商品全部数据函数
def searchall(request):
    goods_list = Goods.objects.all()
    return render(request, 'search_result.html', {'goods_list': goods_list})


# 定义通过商品名称查询数据函数
def searchname(request):
    goods_name = request.GET['goods_name']
    print(goods_name)
    # 完全匹配搜索关键字
    goods_list = Goods.objects.filter(goods_name=goods_name)
    print(goods_list)
    # goods_list Goods.objects.filter(goods_name__contains=goods_name) # 模糊搜索
    return render(request, 'search_result.html', {'goods_list': goods_list})


# 对不同查询结果进行排序的函数
def searchsort(request):
    sort = {'all_asc': Goods.objects.order_by('goods_price'),  # 查询全部结果后升序排列
            'all_desc': Goods.objects.order_by('-goods_price'),  # 查询全部结果后降序排列
            'result_asc': Goods.objects.filter(goods_price__lt='5').order_by('goods_price')  # 对某一查询结果排序
            }
    return render(request, 'search_result.html', {'goods_list': sort[request.GET['sort']]})


# 查询某一价格区间数据视图函数
def searchprice(request):
    min_price = request.GET['min_price']
    max_price = request.GET['max_price']
    goods_lsit = Goods.objects.filter(goods_price__gt=min_price, goods_price__lt=max_price)  # 满足全部多个条件
    # goods_lsit = Goods.objects.filter(Q(goods_price=0.5)|Q(goods_price=2.4)) # 满足任何一个条件
    return render(request, 'search_result.html', {'goods_list': goods_lsit})
