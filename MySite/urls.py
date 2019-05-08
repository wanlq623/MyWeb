from django.urls import path
from MySite import views as views

urlpatterns = [
    path('', views.index),
    path('news_list/<str:news_type>', views.news_list),
    path('filter/', views.fiter_test),
    path('all/', views.searchall),
    path('search_name/', views.searchname),
    path('search_price/', views.searchprice),
    path('search_sort/', views.searchsort),
    path('reg/', views.reg),
    path('register/', views.register),
    path('check/', views.check),
    path('change/', views.change),
    path('change_pass/', views.change_pass),
    path('goods_list/', views.good_list),
    path('add/', views.add),
    path('del/', views.delete),
    path('search/', views.search_price)
]
