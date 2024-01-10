# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test22.py
# @Date   : 2023/12/15 13:37
# @Author : sunpeng
# -----------------------------

class Student(object):
    name = None
    age = None
    addr = None

    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr

    def __str__(self):
        return f"[学生姓名:{self.name},年龄:{self.age},地址:{self.addr}]"


if __name__ == '__main__':
    for i in range(1, 11):
        print(f"当前录入第{i}位学生信息, 总共需要录入10位学生信息")
        name = input("请输入学生姓名:")
        age = int(input("请输入学生年龄:"))
        addr = input("请输入学生地址:")
        s = Student(name, age, addr)
        print(f"学生{i}信息录入完成,信息为:{s}")

