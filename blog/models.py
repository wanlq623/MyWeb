from django.db import models


class Article(models.Model):
    # 文章唯一id
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.CharField(max_length=64)
    # 文章摘要
    brief_content = models.TextField()
    # 文章主要内容
    content = models.TextField()
    # 文章发布日期
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
