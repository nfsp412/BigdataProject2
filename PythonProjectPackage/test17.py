# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test17.py
# @Date   : 2023/12/15 9:50
# @Author : sunpeng
# -----------------------------

"""
异常
"""

f = None
try:
    f = open("datas/2.txt", 'r', encoding='utf8')
except Exception as e:
    print(f"异常{e}")
else:
    print("无异常")
finally:
    f.close()


def f1():
    print("f1开始")
    num = 1 / 0
    print("f1结束")


def f2():
    print("f2开始")
    f1()
    print("f2结束")


def main():
    try:
        f2()
    except Exception as e:
        print(f"异常{e}")


if __name__ == '__main__':
    main()

"""
文件关闭时可能出现异常,例如先f定义为None,所以我们应该先判断一下是否是None
"""
