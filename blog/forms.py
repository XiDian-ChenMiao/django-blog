# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2017 Miao.Chen
# Summary: blog应用中的Form表单模块
from django import forms
from .models import *
from django.core.exceptions import ValidationError


def validate_name(name):
    try:
        publisher = Publisher.objects.get(name=name)
        if publisher:
            raise ValidationError('%s的信息已经存在' % name)
    except Publisher.DoesNotExist:
        pass


class PublisherForm(forms.ModelForm):
    """
    出版社表单类
    """
    name = forms.CharField(label='名称', validators=[validate_name])

    def clean_name(self):
        """
        出版商名称的验证函数
        :return: 
        """
        name = self.cleaned_data['name']
        num_words = len(name.split())
        if num_words < 2:
            raise forms.ValidationError('出版商名称长度不足，需要最少两个字符')
        return name

    class Meta:
        model = Publisher
        exclude = ('id', )


class AuthorForm(forms.ModelForm):
    """
    指定后台作者管理界面显示的表单风格
    """
    class Meta:
        model = Author
        fields = ['name']
        widgets = {
            'name': forms.Textarea(attrs={'cols': '20', 'rows': '1'})
        }
