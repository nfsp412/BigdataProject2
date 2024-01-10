# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test3.py
# @Date   : 2023/12/14 19:22
# @Author : sunpeng
# -----------------------------
import random

if __name__ == '__main__':
    num = random.randint(1, 100)
    index = 0
    while (True):
        guess = int(input("输入数字"))
        if (guess == num):
            print("yes")
            break
        elif (guess > num):
            print("大")
        else:
            print("小")

    print()