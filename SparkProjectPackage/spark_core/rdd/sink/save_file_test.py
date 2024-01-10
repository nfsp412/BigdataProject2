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

# 目录存在会报错
rdd1.saveAsTextFile("/tmp/rdd1")

sc.stop()
