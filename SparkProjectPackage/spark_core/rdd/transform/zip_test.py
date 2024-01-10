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
rdd2 = sc.parallelize((1, 2, 3), numSlices=2)

print(rdd1.zip(rdd2).collect())

sc.stop()
