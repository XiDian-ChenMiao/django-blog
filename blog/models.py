from django.db import models


class Article(models.Model):
    """
    文章
    """
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    title = models.CharField(max_length=64, verbose_name='文章标题')
    content = models.TextField(null=True, verbose_name='文章内容')
    publish_time = models.DateField(auto_now=True, verbose_name='发布时间')

    def __str__(self):
        return self.title


class Publisher(models.Model):
    """
    出版商
    """
    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = '出版商'
        
    name = models.CharField(max_length=70, verbose_name='出版商名称', help_text='出版商名称')
    city = models.CharField(max_length=30, verbose_name='城市', help_text='城市')
    country = models.CharField(max_length=30, verbose_name='国家', help_text='国家')
    
    def __str__(self):
        return self.name
    

class Author(models.Model):
    """
    作者
    """
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'
    
    name = models.CharField(max_length=30, verbose_name='作者名称')

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    书籍
    """
    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'

    name = models.CharField(max_length=50, verbose_name='书籍名称')
    publish_time = models.DateField(verbose_name='出版日期')
    publisher = models.OneToOneField(Publisher, verbose_name='出版商')
    authors = models.ManyToManyField(Author, verbose_name='作者')
    price = models.DecimalField(verbose_name='书籍价格', max_digits=5, decimal_places=2, default=10)

    def __str__(self):
        return self.name


class AuthorDetails(models.Model):
    """
    作者详情
    """
    class Meta:
        verbose_name = '作者详情'
        verbose_name_plural = '作者详情'
    
    city = models.CharField(max_length=30, verbose_name='城市')
    country = models.CharField(max_length=30, verbose_name='国家')
    author = models.ForeignKey(Author, verbose_name='作者')
    email = models.EmailField(verbose_name='邮箱')
    gender = models.BooleanField(verbose_name='性别', max_length=1, choices=[(0, '男'), (1, '女')], default=0)
    website = models.URLField(verbose_name='个人主页', max_length=60, default='')
