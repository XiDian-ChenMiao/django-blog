from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponse
from .forms import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PublisherSerializer
from .models import Publisher


class PublisherView(APIView):
    """
    构建出版商的Restful显示页面
    """
    def get(self, request, format=None):
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data)

    def post(self, request, foramt=None):
        serializer = PublisherSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def publisher_detail(request, pk):
    """
    通过装饰器显示出版商的具体信息
    :param request: 
    :param pk: 
    :return: 
    """
    try:
        publisher = Publisher.objects.get(pk=pk)
    except Publisher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PublisherSerializer(publisher, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    """
    博客首页
    :param request: 
    :return: 
    """
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    """
    通过文章主键ID获取文章内容
    :param request: 
    :param article_id: 
    :return: 
    """
    article = Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


def edit_page(request, article_id):
    """
    文章编辑页面
    :param request: 
    :param article_id: 
    :return: 
    """
    if str(article_id) == '0':
        return render(request, 'blog/article_edit.html')
    article = Article.objects.get(pk=article_id)
    return render(request, 'blog/article_edit.html', {'article': article})


def edit_action(request):
    """
    编辑或者增加新文章
    :param request: 
    :return: 
    """
    title = request.POST['title']
    content = request.POST['content']
    article_id = request.POST['id']
    if str(id) == '0':
        Article.objects.create(title=title, content=content)
        articles = Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    article = Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_edit.html', {'article': article})


def publisher_add(request):
    """
    增加出版商
    :param request: 
    :return: 
    """
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'blog/publisher_list.html', {'publishers': Publisher.objects.all()})
    else:
        form = PublisherForm()
        return render(request, 'blog/publisher_add.html', locals())


def publisher_list(request):
    """
    获取出版商信息
    :param request: 
    :return: 
    """
    return render(request, 'blog/publisher_list.html', {'publishers': Publisher.objects.all()})


def show_request_meta(request):
    """
    显示一次HTTP请求中请求头中的内容
    :param request: 
    :return: 
    """
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse("<table border='1'>%s</table>" % '\n'.join(html))


def set_cookie(request):
    if 'user' in request.COOKIES:
        response = HttpResponse('使用Cookie，键名为：%s的Cookie值为：%s' % ('user', request.COOKIES['user']))
        print(request.COOKIES['user'])
        return response
    else:
        response = HttpResponse('设置Cookie，键名为：%s' % 'user')
        response.set_cookie('user', 'daqinzhidi')
        return response


def login(request):
    """
    测试登录用Session
    :param request: 
    :return: 
    """
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse('登录成功')
        else:
            return HttpResponse('客户端Cookie被禁用')
    request.session.set_test_cookie()
    return render(request, 'blog/login.html')


def auth_login(request):
    """
    认证登录
    :param request: 
    :return: 
    """
    if request.method == 'GET':
        return render(request, 'blog/login.html')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponse('登录成功')
    else:
        return HttpResponse('登录失败，用户名或者密码错误')


def auth_logout(request):
    """
    认证退出
    :param request: 
    :return: 
    """
    auth.logout(request)
    return HttpResponse('用户退出登录')


def register(request):
    """
    注册路由
    :param request: 
    :return: 
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponse('用户注册完成，用户名为：%s' % new_user.username)
    else:
        form = UserCreationForm()
        return render(request, 'blog/register.html', {'form': form})
