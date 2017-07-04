# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2017 Miao.Chen
# Summary: 中间件模块
from django.http import HttpResponse


class CheckSourceMiddleware(object):
    """
    判断请求来源中间件类
    """
    def process_request(self, request):
        """
        请求到来时调用判断访问来源
        :param request: 
        :return: 
        """
        from_source = request.META['HTTP_USER_AGENT']
        print('请求来源', from_source)
        if 'iPhone' in from_source:
            request.session['from_source'] = 'iPhone'
        else:
            request.session['from_source'] = 'PC'

    def process_response(self, request, response):
        """
        响应被发送到客户端之前执行操作
        :param request: 
        :param response: 
        :return: 
        """
        print(request, response)
        return response

    def process_exception(self, request, exception):
        """
        请求发生异常时执行
        :param request: 
        :param exception: 
        :return: 
        """
        print('请求异常', exception)


class ForbidSomeIpMiddleware(object):
    """
    限制主机访问
    """
    def process_request(self, request):
        allow_ip = ['127.0.0.1', ]
        ip = request.META['REMOTE_ADDR']
        print('请求IP', ip)
        if ip not in allow_ip:
            print('该主机被限制访问服务器')
            return HttpResponse('该主机被限制访问服务器')