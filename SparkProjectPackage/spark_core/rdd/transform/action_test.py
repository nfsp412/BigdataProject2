# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : map_test.py
# @Date   : 2023/12/19 22:47
# @Author : sunpeng
# -----------------------------

from pyspark.sql import SparkSession
from pyspark import SparkContext

sc = SparkContext(appName="map", master="local[*]")

rdd = sc.parallelize([1, 2, 1])

# reduce,对元素数据累加计算,无法处理kv类型数据,
print(rdd.reduce(lambda x, y: x + y))

# count,获取元素个数,类比count求和
print(rdd.count())

# take,获取指定个数元素,类比limit
print(rdd.take(1))

# first
print(rdd.first())

# top,排序并指定取出几个元素
print(rdd.top(1))

# takeorder排序后取出
print(rdd.takeOrdered(1))

# 随机取值
print(rdd.takeSample(False, 1))

sc.stop()
