# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test25.py
# @Date   : 2023/12/15 15:30
# @Author : sunpeng
# -----------------------------

"""
继承性
Python中可以实现多继承,即一个类继承多个父类(类似于Java的接口)
同名的成员优先级顺序是从左到右
pass是占位符
无法继承父类的私有成员
调用父类的成员,使用父类名调用,或者使用super()调用
"""


class Phone(object):
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("父类")


class MyPhone(Phone):
    producer = "ITHEIMA"

    print(Phone.producer)

    def call_by_5g(self):
        super().call_by_5g()
        print("子类")


phone = MyPhone()
phone.call_by_5g()
