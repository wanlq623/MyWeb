from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'title', 'brief_content', 'publish_date')


admin.site.register(Article, ArticleAdmin)
