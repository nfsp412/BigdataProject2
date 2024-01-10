# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test16.py
# @Date   : 2023/12/15 9:37
# @Author : sunpeng
# -----------------------------

readf = open("datas/bill.txt", "r", encoding="UTF-8")
writef = open("datas/bill.txt.bak", "w", encoding="UTF-8")

for i in readf:
    if i.strip().split(",")[4] != "测试":
        writef.write(i)

# writef.flush()

readf.close()
writef.close()

"""
close调用时,会自动调用flush
"""

