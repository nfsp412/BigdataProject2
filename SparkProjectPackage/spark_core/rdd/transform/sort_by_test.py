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

# rdd = sc.parallelize([('a', 1), ('a', 2), ('b', 1)])
# sortBy,可以指定排序的字段
# res = rdd.sortBy(lambda x: x[1], ascending=False)

rdd = sc.parallelize([1, 3, 4, 2])
# sortBy可以使用kv类型或者非kv类型的数据集,按照指定字段排序
res = rdd.sortBy(lambda x: x)

print(res.collect())

sc.stop()
