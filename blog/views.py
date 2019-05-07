from django.shortcuts import render
from blog.models import Article
from django.core.paginator import Paginator


# 定义博客首页的文章数据函数
def get_index_page(request):
    # 获取page
    page = request.GET.get('page')
    # 转化page为int类型
    if page:
        page = int(page)
    else:
        page = 1
    # 获取全部文章
    all_article = Article.objects.all()
    # 获取按照时间倒叙排序最新10片文章
    top10_article_list = Article.objects.order_by('-publish_date')[:10]
    # 生成分页组件，每页为4
    paginator = Paginator(all_article, 6)
    # 定义文章数量变量page_num
    page_num = paginator.num_pages
    # 获取某一页的文章列表
    page_article_list = paginator.page(page)
    # 判断是否有下一页，如果有为page+1,否则为page
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    # 判断是否有上一页，如果有为page-1，否则为page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page

    return render(request, 'blog/index.html',
                  {'articles': page_article_list, 'page_num': range(1, page_num + 1), 'curr_page': page,
                   'next_page': next_page, 'previous_page': previous_page, 'top10_article_list': top10_article_list})


# 定义博客详细的数据函数
def get_detail_page(request, article_id):
    # 获取全部文章数据
    articles = Article.objects.all()
    article_contents = None
    previous_article = None
    next_article = None
    # 遍历articles，通过迭代器获取index
    for index, article in enumerate(articles):
        # 上下翻页的判断逻辑
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(articles) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        # 当文章id获取正确，取得文章数据
        if article.article_id == article_id:
            article_contents = article
            previous_article = articles[previous_index]
            next_article = articles[next_index]
            break
    # 格式化文章详细
    content_list = article_contents.content.split('\n')
    # 获取文章标题
    title = article_contents.title
    # 获取时间
    publish_date = article_contents.publish_date
    return render(request, 'blog/detail.html',
                  {'title': title, 'content_list': content_list, 'previous_article': previous_article,
                   'next_article': next_article, 'publish_date': publish_date})


# 定义根据名称搜索文章函数
def search_title(request):
    # 获取输入的搜索title值
    title = request.GET.get('title')
    # 根据title值模糊查询
    article_list = Article.objects.filter(title__contains=title)
    return render(request, 'blog/search_result.html', {'article_list': article_list})
