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

# groupBy可以结合mapValues使用,只分组不聚合,得到的value是迭代器
res = rdd.groupBy(lambda x: hash(x) % 2).mapValues(lambda x: list(x))

print(res.collect())

sc.stop()
