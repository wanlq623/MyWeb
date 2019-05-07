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
]
