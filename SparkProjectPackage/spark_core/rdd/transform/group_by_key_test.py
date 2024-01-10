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

# groupByKey,按照元组的索引0元素作为key进行分组,可以结合mapValues使用,针对kv类型数据使用,在python一般是列表嵌套元组
res = rdd.groupByKey().mapValues(lambda x: list(x))

print(res.collect())

sc.stop()
