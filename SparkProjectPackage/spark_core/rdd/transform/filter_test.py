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

rdd = sc.parallelize([1, 2, 3, 4, 5, 6])

# filter 过滤操作,类比where
res = rdd.filter(lambda x: x == 3)

print(res.collect())

sc.stop()
