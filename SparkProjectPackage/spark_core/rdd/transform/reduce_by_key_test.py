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

rdd = sc.parallelize([('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 3)], numSlices=3)

# reduceByKey,不光分组,还会进行聚合统计,性能更好因为涉及到预聚合
print(rdd.glom().collect())
print(rdd.reduceByKey(lambda x, y: x + y).collect())

# aggregateByKey,分区内和分区间规则可以不同,还存在初始化值
print(rdd.glom().collect())
print(rdd.aggregateByKey(100, lambda x, y: x * y, lambda x, y: x + y).collect())

# foldByKey,存在初始值,但是分区内分区间规则一致
print(rdd.glom().collect())
print(rdd.foldByKey(100, lambda x, y: x + y).collect())

# combineByKey,允许返回值类型和输入值类型不一致
# 例如求key的平均值,中间数值转换成元组,然后分区内累加,分区间合并
print(rdd.glom().collect())
print(rdd.combineByKey(lambda x: (x, 1), lambda x, y: (x[0] + y, x[1] + 1),
                       lambda x, y: (x[0] + y[0], x[1] + y[1])).collect())

sc.stop()
