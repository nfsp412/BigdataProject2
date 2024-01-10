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

# rdd = sc.parallelize(["hadoop hive", "spark python"])
# res = rdd.flatMap(lambda x: x.split(" "))

# flatmap 扁平化处理
rdd = sc.parallelize([{1, 2}, {3, 4}, (5, 6)])
res = rdd.flatMap(lambda x: x)

print(res.collect())

sc.stop()
