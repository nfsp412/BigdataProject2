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

rdd1 = sc.parallelize([('a', 1), ('a', 2), ('b', 1)], numSlices=1)
rdd2 = sc.parallelize((1, 2, 3, 4), numSlices=2)

# union,合并两个rdd,不会去重,求并集
union = rdd1.union(rdd2)
print(union.collect())

# 求交集
inter = rdd1.intersection(rdd2)
print(inter.collect())

# 求差集
subtra = rdd1.subtract(rdd2)
print(subtra.collect())

sc.stop()
