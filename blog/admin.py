from django.contrib import admin

# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    """
    文章后台控制类
    """
    list_display = ['title', 'content', 'publish_time']  # 控制显示的字段
    list_filter = ('publish_time', )  # 在后台管理页面增加按照发布日期的过滤器


admin.site.register(Article, ArticleAdmin)
