# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test33.py
# @Date   : 2023/12/18 21:50
# @Author : sunpeng
# -----------------------------

class MyException(Exception):
    pass


def input_passwd():
    passwd = input("Enter your password: ")
    if len(passwd) >= 8:
        return passwd
    else:
        raise MyException("password is too short")


try:
    input_passwd()
except MyException as e:
    print(e)
