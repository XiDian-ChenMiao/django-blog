# 学习Django总结

## 查询

**使用原生SQL**

extra：修饰查询结果集-一种提供额外查询参数的机制
raw：执行SQL语句

## 中间件工作流程

Django中间件必须是一个类，不需要继承任何类，并实现四个接口：

- process_request(self, request):该方法在请求到来的时候调用；
- process_view(self, request, arg, kwargs):在本次将要执行的View函数被调用前执行；
- process_response(self, request, response):在执行完View函数准备将响应发到客户端前被执行；
- process_exception(self, request, exception):View函数在抛出异常时该函数被调用，得到的exception参数是实际抛出的异常实例。通过该方法可以进行很好的错误控制，提供友好的用户界面。

要激活中间件，需要把它添加到Django配置文件中的`MIDDLEWARE_CLASSES`元组中。