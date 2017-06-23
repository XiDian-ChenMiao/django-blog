# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2017 Miao.Chen
# Summary: 应用blog下的访问地址配置文件

"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)/$', views.edit_page, name='edit_page'),
    url(r'^edit/action/$', views.edit_action, name='edit_action'),
    url(r'^publisher/add/$', views.publisher_add, name='publisher_add'),
    url(r'^publisher/list/$', views.publisher_list, name='publisher_list'),
    url(r'^meta/$', views.show_request_meta, name='show_request_meta'),
    url(r'^cookie/$', views.set_cookie, name='set_cookie'),
    url(r'^login/$', views.login, name='login'),
    url(r'^auth_login/$', views.auth_login, name='auth_login'),
    url(r'^auth_logout/$', views.auth_logout, name='auth_logout'),
    url(r'^register/$', views.register, name='register'),
]