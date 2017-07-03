# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2017 Miao.Chen
# Summary:

from rest_framework import serializers
from .models import Publisher


class PublisherSerializer(serializers.ModelSerializer):
    """
    出版商序列化器
    """
    class Meta:
        model = Publisher
        fields = ['name', 'city', 'country']
