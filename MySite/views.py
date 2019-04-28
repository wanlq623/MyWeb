from django.shortcuts import render
# 从http模块中导入HttpResponse类
from django.http import HttpResponse
from MyWeb import trans

# 定义站点首页视图函数
def index(request):
    # 返回响应内容对象
    return render(request,'index.html')

#定义翻译视图函数
def translate(request):
    from_lang = request.GET['from_lang']
    to_lang = request.GET['to_lang']
    text = request.GET['words']
    return HttpResponse(trans.trans(text,from_lang,to_lang))

#定义翻译2视图函数
def translate2(request,words,from_lang,to_lang):
    return HttpResponse(trans.trans(words,from_lang,to_lang))

#定义新闻列表视图
def news_list(request,news_type):
    #创建参数字典
    news_dict = {'economic':'经济','sport':'体育'}
    news_titles = []
    if news_type == 'economic':
        news_titles = [('12/5', '作者成为全国首富。'), ('12/4', '作者成为全省首富。'),
                       ('12/3', '作者成为全市首富。'), ('12/2', '作者成为镇里首富。'), ('12/1', '作者成为村里首富。')]
    #整合数据并返回页面内容
    return render(request,'news_list.html',{'news_type':news_dict[news_type],'news_titles':news_titles})

#定义过滤器测试视图
def fiter_test(request):
    return render(request,'filter.html',{'letters':'abc','number':1})
