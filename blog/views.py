from django.shortcuts import render, render_to_response
from .models import Article


def index(request):
    """
    博客首页
    :param request: 
    :return: 
    """
    articles = Article.objects.all()
    return render_to_response('blog/index.html', {'articles': articles})


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
