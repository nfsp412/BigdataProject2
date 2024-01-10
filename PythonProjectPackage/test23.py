# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test23.py
# @Date   : 2023/12/15 13:47
# @Author : sunpeng
# -----------------------------

"""
封装性:
私有成员变量,私有成员方法,以两个下划线__开头定义
"""


class Phone(object):
    IMEI = None
    producer = None
    __current_voltage = None

    def call_by_5g(self):
        print("5g通话已开启")

    def __keep_single_core(self):
        print("让CPU以单核模式运行以节省电量")

    def get_current_voltage(self):
        return self.__current_voltage

    def set_current_voltage(self, current_voltage):
        self.__current_voltage = current_voltage


phone = Phone()
# 无法使用私有成员方法,会报错
# phone.__keep_single_core()
# 无法使用私有成员变量
# print(__current_voltage)
# 不会报错,但是没有效果
# phone.__current_voltage = 33

# 通过getset方法访问
phone.set_current_voltage(100)
print(phone.get_current_voltage())

