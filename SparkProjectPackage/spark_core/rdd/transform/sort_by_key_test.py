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

# sortByKey,自动按照key值进行排序,默认升序,ASCII码值,不会排序元组的其他数据(value),针对kv类型数据使用
res = rdd.sortByKey(ascending=False)

print(res.collect())

sc.stop()
