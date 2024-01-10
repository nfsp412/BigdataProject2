# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test32.py
# @Date   : 2023/12/18 14:24
# @Author : sunpeng
# -----------------------------

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __del__(self):
#         print("销毁")
#
#
# cat = Cat("tom")


class MusicPlayer(object):
    # 定义类属性,记录第一个被创建的对象的引用
    instance = None

    # 初始化方法执行标识
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 判断是否已经创建对象
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if MusicPlayer.init_flag:
            return
        MusicPlayer.init_flag = True
        pass


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)


class Person(object):
    count = None

    @classmethod
    def f1(cls):
        print(cls.count)

    @staticmethod
    def f2():
        pass


person = Person()
print(person)
