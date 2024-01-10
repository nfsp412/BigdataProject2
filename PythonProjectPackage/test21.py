# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test21.py
# @Date   : 2023/12/15 11:13
# @Author : sunpeng
# -----------------------------

"""
面向对象

类的定义:
class Person:
class Person():
class Person(继承父类):

注意,定义在类内部的函数,称为成员方法
    定义成员方法时,自动携带self,调用成员变量必须使用self进行调用,传参时忽略
变量称为成员变量

构造方法,用来初始化一些成员变量
    使用__init__接收参数,创建对象时将参数写在()小括号中,这样就完成初始化

魔术方法:
    __init__ 即Java构造器
    __str__ 即Java的toString重写
    __lt__ 即Java比较器
    __le__ 即Java比较器
    __eq__ 即Java的equals方法重写

面向对象三大特性:
封装性:
继承性:
多态性:
"""


class Person(object):
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(f"Hello, {self.name}, {self.age}")


person = Person("张三", 19)
person.hello()
