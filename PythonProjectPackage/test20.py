# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test20.py
# @Date   : 2023/12/15 10:51
# @Author : sunpeng
# -----------------------------

"""
使用json模块

json格式:[{},{},{}]或者{}

import json
"""

import json

# 列表
data = [{"name": "张三", "age": 20}, {"name": "李四", "age": 21}]
# 字符串
data2 = "{\"name\":\"张三\"}"
# 字典
data3 = {"name": "张三", "age": 18}
print(data, type(data))
print(data2, type(data2))
print(data3, type(data3))

# 将python的列表+字典转换成json
data_json = json.dumps(data, ensure_ascii=False)
# 将python的字符串转换成json
data2_json = json.dumps(data2, ensure_ascii=False)
# 将python的字典转换成json
data3_json = json.dumps(data3, ensure_ascii=False)

# 进行编码,使用ensure_ascii=False解决
# json本质上是字符串类型
print(data_json, type(data_json))
print(data2_json, type(data2_json))
print(data3_json, type(data3_json))

# 解码
data_new = json.loads(data_json)
data2_new = json.loads(data2_json)
data3_new = json.loads(data3_json)

# 解码后
print(data_new, type(data_new))
print(data2_new, type(data2_new))
print(data3_new, type(data3_new))

