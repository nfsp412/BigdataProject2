# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test26.py
# @Date   : 2023/12/15 16:24
# @Author : sunpeng
# -----------------------------

"""
类型注解, 类比Java的泛型，但是不会进行校验
方便开发
变量的类型注解:基本数据类型,容器,类
方法的类型注解:形参注解,返回值注解
Union联合注解, 例如list中有多种数据类型, 那么如何描述?
"""


class Student:
    pass


s: Student = Student()

v1: int = 10
v2: float = 1.1
v3: bool = True
v4: str = "ABC"

l1: list = [1, 2, 3]
t1: tuple = (1, 2, 3)
s1: set = {1, 2, 3}
d1: dict[str, int] = {"a": 1, "b": 2, "c": 3}


def f1(x: int, y: int) -> int:
    """

    :param x:
    :param y:
    :return:
    """
    return x + y


print(f1(1, 2))

from typing import Union

my_list: list[Union[str, int, bool]] = [1, "2", True]

