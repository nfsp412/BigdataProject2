# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test31.py
# @Date   : 2023/12/17 12:22
# @Author : sunpeng
# -----------------------------

dict1 = {
    "name": "zhangsan",
    "age": 18,
    "addr": "beijing"
}

for i in dict1:
    print(i, dict1[i])


def f1(*args):
    print(args)


# 会把整个元组当做一个元素
t1 = (1, 2, 3)
f1(t1)

print(dir(object))

print(dir(f1))

