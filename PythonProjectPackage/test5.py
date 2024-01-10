# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test5.py
# @Date   : 2023/12/14 19:36
# @Author : sunpeng
# -----------------------------
import random

if __name__ == '__main__':
    """
    for 遍历循环
    字符串就是可以遍历的
    """
    """
    range [a,b) 左闭右开
    默认从0开始
    第三个参数是步长
    """
    for i in range(1, 10):
        print(i)

    name = "abcde"
    for i in name:
        print(i)

    sum = 0
    s1 = "itheima is a brand of itcast"
    for i in s1:
        if i == "a":
            sum = sum + 1

    print(sum)

    """
    可迭代类型有 字符串 列表 元组等
    """

    num = 100
    res = 0
    for i in range(1, num):
        if i % 2 == 0:
            res += 1
    print(res)
    """
    关于变量的作用域, 可以访问内部的i变量,但是不建议这样使用,应该在外部事先声明一个变量
    """
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{i}*{j}={i * j}", end=" ")
        print()

    sum = 10000
    for i in range(1, 21):
        sc = random.randint(1, 10)
        if sc < 5:
            print(f"员工{i},绩效{sc},不发工资")
            continue
        else:
            sum -= 1000
            print(f"员工{i},工资1000")
            if sum <= 0:
                print(f"当前发完{i}员工,工资不足结束发放")
                break
