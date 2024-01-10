# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : my_module1.py
# @Date   : 2023/12/15 10:15
# @Author : sunpeng
# -----------------------------

__all__ = ['test']


def test(x, y):
    print(x + y)


def test2(x, y):
    print(x - y)


if __name__ == '__main__':
    test(1, 2)
    test2(1, 2)
