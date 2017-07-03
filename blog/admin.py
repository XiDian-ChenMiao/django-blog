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
    from .forms import AuthorForm
    form = AuthorForm  # 指定后台管理页面绑定的表单

    def print_author_action(self, request, queryset):
        """
        对于作者的打印动作
        :param modeladmin: 
        :param request: 
        :param queryset: 
        :return: 
        """
        for item in queryset:
            print(item)
        self.message_user(request, "%d位作者信息被打印。" % len(queryset))

    print_author_action.short_description = '打印对象'
    actions = [print_author_action]  # 指定后台对于对象的动作


def global_show_action(modeladmin, request, queryset):
    """
    全局打印函数
    :param modeladmin: 
    :param request: 
    :param queryset: 
    :return: 
    """
    for item in queryset:
        print(item)
    modeladmin.message_user(request, "%d objects were showed." % len(queryset))


admin.site.register(Article, ArticleAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.add_action(global_show_action, '全局打印')
