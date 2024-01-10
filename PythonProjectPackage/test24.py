# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test24.py
# @Date   : 2023/12/15 15:27
# @Author : sunpeng
# -----------------------------

"""

"""

class Phone(object):
    __is_5g_enable = None
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()
phone.call_by_5g()