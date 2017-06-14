from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    """
    文章后台控制类
    """
    list_display = ['title', 'content', 'publish_time']  # 控制显示的字段
    list_filter = ('publish_time', )  # 在后台管理页面增加按照发布日期的过滤器


class PublisherAdmin(admin.ModelAdmin):
    """
    出版商后台控制类
    """
    list_display = ['name', 'city', 'country']  # 控制显示的字段
    search_fields = ('name', 'city')  # 搜索字段
    list_filter = ('city', )  # 过滤字段
    fieldsets = (
        (None, {'fields': ('name', )}),
        ('高级属性', {'fields': ('city', 'country'), 'classes': ('collapse', )})
    )  # 编辑页面的分组


class BookAdmin(admin.ModelAdmin):
    """
    书籍后台控制类
    """
    list_display = ['name', 'publish_time', 'publisher']  # 控制显示的字段
    list_filter = ('publish_time', )  # 在后台管理页面增加按照发布日期的过滤器


class AuthorAdmin(admin.ModelAdmin):
    """
    作者后台控制类
    """
    list_display = ['name']  # 控制显示的字段


admin.site.register(Article, ArticleAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
