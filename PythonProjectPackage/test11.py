# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test11.py
# @Date   : 2023/12/14 22:33
# @Author : sunpeng
# -----------------------------

"""
set 集合
用来去重,是无序的
无序:每次打印的结果都不一样的顺序
定义:字面量,大括号,set()
set()可以传入字符串序列,list,tuple
"""
s1 = {1, 2, 3}
s2 = {}
s3 = set("abcc")
print(s1)
print(s2)
print(s3)
print(set([1, 2, 3]))
t1 = (1, 2, 3)
l1 = [1, 2, 3]
print(set(t1))
print(set(l1))
"""
集合无序,所以不支持索引
增删改查
"""
# 添加元素add
s3.add("abc")
print(s3)
# 删除元素remove
s3.remove("abc")
print(s3)
# 随机删除元素,和list区别在于,无法指定索引,但是都会有返回值
# 每次打印的结果都不一样
a = s3.pop()
print(s3)
print(a)
# 清空集合,打印的是set(),而不是(),为了区分元组
s3.clear()
print(s3)
# 元素个数len
print(len(s3))
# 可以遍历,但是不能使用while,因为没有索引
s3 = {1, 2, 3}
for i in s3:
    print(i)

my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']

s1 = set()
for i in my_list:
    s1.add(i)
print(s1)

s2 = set(my_list)
print(s2)
