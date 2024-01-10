# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : row_test.py
# @Date   : 2023/12/20 15:56
# @Author : sunpeng
# -----------------------------

from pyspark.sql import Row

# 本质上是一个元组
r1 = Row(1001, "张三", 20)

print(r1[0])
print(r1[1])
print(r1[2])

# 可以使用关键字参数
r2 = Row(id=1002, name="李四", age=23)
print(r2["id"])
print(r2["name"])
print(r2["age"])
