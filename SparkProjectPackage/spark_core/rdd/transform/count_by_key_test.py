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

rdd = sc.parallelize([('a', 1), ('a', 2), ('b', 1)])

print(rdd.countByKey())
print(rdd.countByKey().items())
print(rdd.countByKey().keys())
print(rdd.countByKey().values())

sc.stop()

