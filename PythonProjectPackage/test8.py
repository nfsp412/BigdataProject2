# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test8.py
# @Date   : 2023/12/14 21:47
# @Author : sunpeng
# -----------------------------

"""
元组tuple
一旦定义完成后, 就不能被修改
定义:
字面量
(),注意一个元素时候,必须有逗号
tuple()
"""
t1 = (1, 2, 3)
t2 = ()
t3 = tuple()
t4 = tuple([1])
t5 = tuple([1, 2, 3])

"""
index查询元素
count统计元素
len求长度
使用索引查询元素,或者index查询索引
"""
print(t1.index(1))
print(t1.count(1))
print(len(t1))

t1 = ('周杰伦', 11, ['football','music'])
print(t1.index(11))
print(t1[0])
del t1[2][0]
print(t1)
t1[2].append('coding')
print(t1)

