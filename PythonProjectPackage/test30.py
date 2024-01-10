# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test30.py
# @Date   : 2023/12/16 18:36
# @Author : sunpeng
# -----------------------------

"""
闭包和装饰器
"""
import os
import re

# 不使用闭包
account_amount = 0


def atm(num, deposit=True):
    global account_amount
    if deposit:
        account_amount += num
        print(f"存款{num}, 账户余额{account_amount}")
    else:
        account_amount -= num
        print(f"取款{num}, 账户余额{account_amount}")


atm(300)
atm(300)
atm(100, False)


# 问题: 全局变量可能被修改

# 使用闭包
def account_create(initial_amount=0):
    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款{num}, 账户余额{initial_amount}")
        else:
            initial_amount -= num
            print(f"取款{num}, 账户余额{account_amount}")

    return atm


fn = account_create()
fn(300)
fn(200)
fn(300, False)


# 闭包:有嵌套,有引用,有返回

def outer(logo):
    def inner(msg):
        print("{logo}-{msg}".format(logo=logo, msg=msg))

    return inner


fn = outer(logo="abc")
fn("def")
fn("ghi")


# 演示nonlocal
def outer(num1):
    def inner(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner


fn = outer(num1=10)
fn(10)
fn(10)
fn(10)
fn(10)

"""
装饰器:本质是闭包,用来不破坏目标函数的原有代码和功能,为目标函数增加功能
"""


# 不使用装饰器
def sleep():
    import random
    import time
    print("睡眠中...")
    # time.sleep(random.randint(1, 5))


sleep()
# 为sleep函数增加功能
print("开始睡觉")
sleep()
print("结束睡觉")


# 使用闭包:更优雅
def outer(func):
    def inner():
        print("开始睡觉")
        func()
        print("结束睡觉")

    return inner


fn = outer(sleep)
fn()


# 使用语法糖@
@outer
def f1():
    print("装饰器语法糖")


f1()

"""
单例模式: 只需要一个类的实例对象
"""


class Tool(object):
    pass


t1 = Tool()
t2 = Tool()
# 可以发现内存地址不同,即创建了两个对象
print(t1)
print(t2)

# 如何实现单例模式:在一个文件中定义某个类,并且创建对象;在需要引用的地方,from 文件 import 对象, 这样就实现了单例模式
from single1 import tool

t1 = tool
t2 = tool
print(t1, t2)

"""
工厂模式:当需要创建一个类的大量的实例对象时,使用
"""


# 不使用工厂模式
class Person(object):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class Worker(Person):
    pass


worker = Worker()
student = Student()
teacher = Teacher()


# 使用工厂模式
class Factory(object):
    def get_object(self, type):
        if type == "Student":
            return Student()
        elif type == "Teacher":
            return Teacher()
        elif type == "Worker":
            return Worker()


factory = Factory()
factory.get_object("Student")
factory.get_object("Teacher")
factory.get_object("Worker")
# 优点:创建对象的大批量操作有了一个统一入口,易于维护,仅仅修改工厂类中创建对象的方式即可,

"""
多线程
target:执行的目标任务名称,例如函数名
args:元组传参
kwargs:字典传参
"""
import threading


def sing(*args, **kwargs):
    print("sing")
    print(args)


def dance(*args, **kwargs):
    print("dance")
    print(kwargs)


obj1 = threading.Thread(name="线程1", target=sing, args=("1",))
obj2 = threading.Thread(name="线程2", target=dance, kwargs={"k1": "v1"})
obj1.start()
obj2.start()

"""
socket编程,服务器端
"""
import socket

# # 1.创建对象
# s = socket.socket()
# # 注意是元组
# # 2.绑定端口地址
# s.bind(("localhost", 8888))
# # 3.监听端口
# s.listen()
# # 4.接收客户端请求
# # accept阻塞方法,接收两个参数
# conn, address = s.accept()
# print(f"接收客户端请求,连接来自{address}")
# # 接收客户端发来的消息
# # 接收字节数组,使用utf8解码
# while True:
#     data = conn.recv(1024).decode("utf-8")
#     if data == 'exit':
#         break
#     print(f"接收数据,{data}")
#     # 回复消息
#     str1 = "你好"
#     conn.send(str1.encode(encoding="utf-8"))
#
# 5.关闭
# s.close()
# conn.close()

"""
客户端开发
"""
# 1.创建对象
# s = socket.socket()
# # 2.连接服务器
# s.connect(("127.0.0.1", 8888))
# # 3.发送消息
# while True:
#     msg = input("输入消息:")
#     if msg == "quit":
#         break
#     s.send(msg.encode("utf-8"))
#
#     rec = s.recv(1024).decode("utf8")
#     # recv方法是阻塞的
#     print("服务器器消息:", rec)
# # 4.关闭
# s.close()

"""
正则表达式模块: re
"""
s = "python itheima python itheima python itheima python"
# match 从头开始匹配  严格匹配 匹配成功返回匹配对象, 不成功返回空
# <re.Match object; span=(0, 6), match='python'>
res = re.match('python', s)
print(res)
# 匹配的索引位置,包左不包右
print(res.span())
# 返回匹配内容
print(res.group())
# search 从头匹配,全局匹配,匹配到第一个成功就返回
res2 = re.search('itheima', s)
print(res2)
print(res2.span())
print(res2.group())
# findall 匹配所有能成功匹配的内容,返回的是list,没有的就返回空list
res3 = re.findall('itheima', s)
print(res3)

"""
高级正则
单个字符的匹配
. 匹配任意一个字符,除了\n
[] 匹配列举的字符
\d 匹配数字
\D 匹配非数字
\s 匹配空格,制表
\S 匹配非空白
\w 匹配数字字母下划线
\W 匹配非单词字符
"""
s = ".itheima1@!\!!66#  #"
print(re.findall(r'\d', s))
print(re.findall(r'\D', s))
print(re.findall(r'\w', s))
print(re.findall(r'\W', s))
print(re.findall(r'\s', s))
print(re.findall(r'\S', s))
print(re.findall(r'[\s]', s))
print(re.findall(r'.', s))
print(re.findall(r'\.', s))
"""
* 代表前面的字符匹配0或无数
+ 代表前面的字符匹配1或者无数
? 代表前面的字符匹配0或1
{m} 代表前面的字符匹配m次数
{m,} 代表至少m次
{m,n} 代表出现m到n次

^ 匹配字符串开头
$ 匹配字符串结尾
\b 匹配单词边界
\B 匹配非单词边界

| 代表或者
() 代表匹配一个整体
"""

"""
递归和os模块
"""
# 列举所有文件,包含隐藏
print(os.listdir("C:/"))
# 判断是否是文件夹目录
print(os.path.isdir("C:/sunpeng"))
# 判断目录是否存在
print(os.path.exists("C:/sunpeng"))
