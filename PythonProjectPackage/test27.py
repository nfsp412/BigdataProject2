# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test27.py
# @Date   : 2023/12/15 16:48
# @Author : sunpeng
# -----------------------------

"""
多态
抽象类,或者说接口,父类中的方法是pass的,就类比Java的抽象类和接口
"""


class Animal(object):
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("wang")


class Cat(Animal):
    def speak(self):
        print("miao")


def make(animal: Animal):
    animal.speak()


if __name__ == '__main__':
    """
    传入不同的子类对象,实现不同的效果
    """
    dog: Animal = Dog()
    cat: Cat = Cat()

    make(dog)
    make(cat)

