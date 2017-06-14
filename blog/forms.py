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

    class Meta:
        model = Publisher
        exclude = ('id', )
