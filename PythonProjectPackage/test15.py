# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test15.py
# @Date   : 2023/12/15 9:24
# @Author : sunpeng
# -----------------------------

"""
文件的写入,在open时,使用w
文件的追加,使用a
注意write写入并没有真正写入,必须flush刷新buffer才可以
注意换行符等特殊字符
"""

with open("datas/test.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")
    f.write("hello")
    f.flush()

with open("datas/test.txt", "a", encoding="utf-8") as f:
    f.write("hi")
    f.flush()



