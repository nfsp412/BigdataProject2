# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : str_util.py
# @Date   : 2023/12/15 10:31
# @Author : sunpeng
# -----------------------------


def str_reverse(s):
    """
    Reverse the string
    :param s: input a string
    :return: output a reversed string
    """
    return s[::-1]


def substr(s, x, y):
    """
    Substract the string [x, y]
    :param s: input a string
    :param x: start position
    :param y: end position
    :return: output a sub string
    """
    return s[x:y + 1]


if __name__ == '__main__':
    print(str_reverse("abc"))
    print(substr("abcde", 2, 3))
