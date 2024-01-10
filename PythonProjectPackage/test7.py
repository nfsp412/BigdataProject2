# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test7.py
# @Date   : 2023/12/14 20:56
# @Author : sunpeng
# -----------------------------

"""
数据容器:批量存储数据使用
按照是否可以重复元素, 是否可以修改, 是否有序进行分类
list列表
tuple元组
str字符串
set集合
dict字典
"""

"""
list列表:
定义列表: 三种方式
打印列表: 直接打印字面量
可以重复, 可以多种类型, 可以嵌套
list()定义列表, 把字符串可以拆分开
"""
l1 = [1, 2, 3]
l2 = []
l3 = list()

print(l1, l2, l3)

print(list(["a", True, 1]))
print(["a", True, 1])
print(list(l1))
print(list("abc"))

"""
list的索引, 从0或-1开始
"""
print(l1[0])
print(l1[-1])

"""
list的增删改查
"""
"""
函数和方法, 单独定义的是函数, 定义在类中的叫方法
"""
# index查询不到报错
# 使用索引查询元素,或者使用index查询索引
print(l1.index(1))
# 修改,使用索引修改元素
l1[0] = 100
print(l1[0])
# insert插入元素,在指定索引位置插入元素,顺序向后移动
#
l1.insert(0, "a")
print(l1)
# 即使插入索引10,由于list是连续的,所以实际上并不是插入的该位置,而是索引4
# l1.insert(10,100)
# print(l1[10])
# 追加元素到末尾append
l1.append("a")
print(l1)
# 追加元素extend,会将字符串这种遍历追加,而append会视为整体
l1.extend([1, 2, 3])
print(l1)
l1.extend("abc")
print(l1)
l1.append("abc")
print(l1)
# 删除元素
del l1[0]
print(l1)
# 使用pop删除,可以指定索引删除
a = l1.pop(3)
print(f"删除元素{a}")
print(l1)
# 按照元素进行删除remove
l1.remove("abc")
print(l1)
# 统计list中某个元素的个数
print(l1.count(1))
# 统计列表的长度,即元素个数
print(len(l1))
# 清空整个列表的元素,但是列表还存在
l1.clear()
print(l1)
for i in [1, 2, 3]:
    print(i)
l1 = [1, 2, 3]
for i in l1:
    print(i)

l1[1] = 100
print(l1)

l4 = [21, 25, 21, 23, 22, 20]
l4.append(31)
print(l4)
l4.extend([29, 33, 30])
print(l4)
print(l4[0])
print(l4[-1])
print(l4)
print(l4.index(31))
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = []
for i in l1:
    if i % 2 == 0:
        l2.append(i)
print(l2)

index = 0
while index < len(l1):
    if l1[index] % 2 == 0:
        l2.append(l1[index])
    index += 1
print(l2)

