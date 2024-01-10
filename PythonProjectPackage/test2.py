# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test2.py
# @Date   : 2023/12/14 19:10
# @Author : sunpeng
# -----------------------------
import random

if __name__ == '__main__':
    """
    random, randint 范围[1,10]
    闭区间
    """
    a = random.randint(1, 10)
    b = int(input("第一次"))
    if a == b:
        print("yes")
    else:
        b = int(input("第2次"))
        if a == b:
            print("yes")
        else:
            b = int(input("第3次"))
            if a == b:
                print("yes")
            else:
                print("三次用完")
