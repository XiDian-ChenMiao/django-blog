# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2017 Miao.Chen
# Summary: 项目中涉及到的信号机制

from django.dispatch import Signal, receiver
from django.db.models.signals import pre_save, post_save
from .models import Publisher, Author


sigal_a = Signal(providing_args=['name'])


def signal_callback(sender, **kwargs):
    """
    信号处理回调
    :param sender: 
    :param kwargs: 
    :return: 
    """
    print(sender, kwargs)
    print('signal_callback called')


@receiver(sigal_a)
def signal_show(sender, **kwargs):
    pass


@receiver(pre_save, sender=Publisher)
def signal_pre_save_callback(sender, **kwargs):
    """
    模型保存前的回调
    :param sender: 
    :param kwargs: 
    :return: 
    """
    pass


@receiver(post_save, sender=Author)
def signal_post_save_callback(sender, **kwargs):
    """
    模型保存后的回调
    :param sender: 
    :param kwargs: 
    :return: 
    """
    pass


sigal_a.connect(signal_callback)
