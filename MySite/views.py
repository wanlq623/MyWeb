from django.shortcuts import render
# 从http模块中导入HttpResponse类
from django.http import HttpResponse
from MyWeb import trans
from MySite.models import Goods
from django.db.models import Q
from MySite.models import Users
import json
from MySite.models import GoodsInfo
from django.core import serializers


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


# 打开注册页面函数
def reg(request):
    return render(request, 'register.html')


# 检查用户名是否注册的函数
def check(request):
    user_name = request.GET.get('user_name')
    user = Users.objects.filter(username=user_name)
    if user:
        # 已注册
        status = 100
    else:
        # 未注册
        status = 200
    return HttpResponse(status)


# 实现注册函数
def register(request):
    user_name = request.GET.get('user_name')
    password = request.GET.get('password')
    try:
        user = Users(username=user_name, password=password)
        user.save()
        status = 200  # 注册成功
    except:
        status = 100  # 注册失败
    return HttpResponse(json.dumps({'status': status}))


# 打开修改密码页面
def change(request):
    return render(request, 'change.html')


# 实现密码修改函数
def change_pass(request):
    user_name = request.GET.get('user_name')
    password = request.GET.get('password')
    # 查询已存在用户的数据对象
    user = Users.objects.filter(username=user_name)
    try:
        user.update(password=password)  # 更新数据库密码
        status = 200
    except:
        status = 100
    return HttpResponse(json.dumps({'status': status}))


# 定义查询商品信息的函数
def good_list(request):
    goods_list = GoodsInfo.objects.all()
    return render(request, 'good_list.html', {'goods_list': goods_list})


# 定义添加商品的函数
def add(request):
    goods_name = request.GET.get('goods_name')
    goods_price = request.GET.get('goods_price')
    goods_number = request.GET.get('goods_number')
    isexist = GoodsInfo.objects.filter(goods_name=goods_name)
    try:
        if not isexist:
            goods = GoodsInfo()
            goods.goods_name = goods_name
            goods.goods_price = goods_price
            goods.goods_number = goods_number
            goods.save()
            result = 200
        else:
            result = 100
    except:
        result = 100
    return HttpResponse(result)


# 定义删除商品函数
def delete(request):
    goods_name = request.GET.get('goods_name')
    goods = GoodsInfo.objects.filter(goods_name=goods_name)
    try:
        goods.delete()
        result = 200
    except:
        result = 100
    return HttpResponse(result)


# 定义价格区间查询函数
def search_price(request):
    min_price = int(request.GET.get('min_price'))
    max_price = int(request.GET.get('max_price'))
    goods = GoodsInfo.objects.filter(goods_price__gte=min_price, goods_price__lte=max_price)
    try:
        if goods:
            result = json.dumps(serializers.serialize('json', goods))
        else:
            result = 100
    except:
        result = 100
    return HttpResponse(result)
