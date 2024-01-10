# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test12.py
# @Date   : 2023/12/14 22:51
# @Author : sunpeng
# -----------------------------

"""
字典 dict
定义
字面量
{}大括号
dict()
"""
import random

d1 = {"k1": "v1", 1: 1}
print(d1)
d2 = {}
print(d2)
d3 = dict(k1=1, k2=2)
print(d3)
"""
key不能重复
key和value可以是任何类型
key不能是字典,value可以是
"""
"""
通过key修改或者添加value,key存在就是修改,key不存在就是添加
根据key删除元素,使用pop(key)
clear清空字典
keys获取全部的key,然后for遍历所有的key获取key和value
len获取kv键值对数量
"""
print(d1["k1"])

d1 = {
    "王力宏": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周杰伦": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 2
    }
}
print(d1)
for i in d1.keys():
    if d1.get(i).get("级别") == 1:
        sal = d1.get(i).get("工资")
        sal += 1000
        d1[i]["工资"] = sal
print(d1)

"""
数据容器对比:
支持索引:字符串,list,tuple
支持重复:字符串,list,tuple
可以修改:list,set,dict
"""

"""
容器的通用功能:len求长度,max,min,for循环遍历,类型转换list()set()str()tuple()
排序sorted,默认升序,reverse=True降序
会得到list
"""
print(sorted("abc", reverse=True))

"""
关于max和min,字符串之间如何比较?
按照每一位字符进行比较,只要比较出来大小,就不会继续比较了
按照ASCII码进行比较
"""
print(max("abc", "abd"))

number = 8
nums = []
lucky = []
for i in range(1,number+1):
    nums.append(i)
    if i % 6 == 0:
        lucky.append(i)

print(nums)
print(lucky)

teachers = ['A','B','C','D','E','F','G','H']
classroom = [[],[],[]]
for teacher in teachers:
    index = random.randint(0,2)
    classroom[index].append(teacher)

print(classroom)


