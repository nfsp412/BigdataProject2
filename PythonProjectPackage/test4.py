# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test3.py
# @Date   : 2023/12/14 19:22
# @Author : sunpeng
# -----------------------------
import random

if __name__ == '__main__':
    """
    print进阶:
    sep分隔符默认空格
    end结束符默认换行
    使用\t可以对齐数据
    """
    i = 1
    while i <= 9:

        j = 1
        while j <= i:

            print(f"{i}*{j}={i*j}", end=' ')

            j += 1

        print()

        i += 1

