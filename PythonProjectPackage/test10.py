# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test10.py
# @Date   : 2023/12/14 22:12
# @Author : sunpeng
# -----------------------------

"""
序列的切片
序列:字符串,list,tuple
步长N,代表跳过N-1个元素
[起始索引, 结束索引)
序列的切片会得到一个新的序列
"""

"""
步长为正,代表从正向开始,如果不写开头,那么从索引0
步长为负,代表从负向开始,如果不写开头,那么从索引-1开始
结束位置和开始位置可以正可以负,找到即可
如果不写结束,那么步长为正则到正向结束,步长为负则到负向结束
"""
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l1[-2:-4:-1])
print(l1[-2:4:-1])
print(l1[-2::-1])

str1 = "万过薪月，员序程马黑来，nohtyP学"
print(str1[9:4:-1])

