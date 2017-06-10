from django.db import models


class Article(models.Model):

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    title = models.CharField(max_length=64, default='标题')
    content = models.TextField(null=True)
    publish_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
