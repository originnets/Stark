from django.db import models
from django.conf import settings

# Create your models here.



# class Article(models.Model):
#     title = models.CharField(max_length=200)  #博客标题
#     category = models.ForeignKey('Category', verbose_name="文章类型", on_delete=models.CASCADE)  # 类别
#     date_time = models.DateField(auto_now_add=True)  # 博客日期
#     content = models.TextField(blank=True, null=True)  # 文章正文
#     digest = models.TextField(blank=True, null=True)  # 文章摘要
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)  # 作者
#     view = models.BigIntegerField(default=0)  # 阅读数
#     comment = models.BigIntegerField(default=0)  # 评论数
#     picture = models.CharField(max_length=200)  # 标题图片地址
#     tag = models.ManyToManyField(Tag)  # 标签
#
#     def __str__(self):
#         return self.title

class Article(models.Model):
    ar_name = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    date_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ar_name
