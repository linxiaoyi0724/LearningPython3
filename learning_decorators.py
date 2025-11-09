# 装饰器允许在不修改原有函数代码的基础上，动态的增加或者修改函数的功能，本质是一个接收函数作为输入并返回一个新的包装过后的函数的对象

'''
# 装饰器demo
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"在原函数前执行")
        func()
        print(f"在原函数后执行")
    return wrapper

@my_decorator
def say_hello():
    print(f"hello")

say_hello()
'''
from pty import spawn
from tkinter.font import names

'''
# 将函数参数传入装饰器
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"before call original function")
        func(*args, **kwargs)
        print(f"after call original function")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello {name}")
greet("muzhen")
'''

'''
# 装饰器本身接收参数
def repeat(num_times):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return my_decorator

@repeat(3)
def say_hello(name):
    print(f"hello {name}")

say_hello('muzhen')
'''


# 类装饰器有两种形式，函数形式的类装饰器跟类形式的类装饰器

'''
# 函数形式的类装饰器
def log_class_decorator(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs) #实例化原有的类

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

        def display(self):
            print(f"调用cls.__name__.display() 前")
            self.wrapped.display()
            print(f"调用cls.__name__.display() 后")
    return Wrapper

@log_class_decorator
class MyClass:
    def display(self):
        print(f"这是MyClass的display的方法")
obj = MyClass()
obj.display()
'''


'''
# 类形式的类装饰器
class SingletonDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance

@SingletonDecorator
class MyClass:
    def __init__(self):
        print(f"MyClass 初始化")

mc1 = MyClass()
mc2 = MyClass()
print(mc1 is mc2)
'''


'''
#内置装饰器
class MyClass:
    @staticmethod
    def static_method():
        print(f"This is a static method")

    @classmethod
    def class_method(cls):
        print(f"This is a class method")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

MyClass.class_method()
MyClass.static_method()

obj = MyClass()
obj.name = 'muzhen'
print(f"obj.name is {obj.name}")
'''


# 多个装饰器堆叠
def decorator1(func):
    def wrapper(*args, **kwargs):
        print(f"this is decorator1")
        func(*args, **kwargs)
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print(f"this is decorator2")
        func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def say_hello(name):
    print(f"hello {name}")

say_hello('muzhen')










