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

rdd1 = sc.parallelize([('a', 1), ('a', 2), ('d', 1)])
rdd2 = sc.parallelize([('a', 4), ('a', 5), ('c', 6)])

# join,类似于内连接
print(rdd1.join(rdd2).collect())

# left outer join,类似于左外连接
# 保留左边表所有数据,右表关联不上的数据填充None
print(rdd1.leftOuterJoin(rdd2).collect())

# cogroup,并不是关联了,而是把key相同的两个rdd中的value数据都汇总到一起,关联不上的也能获取到一起
print(rdd1.cogroup(rdd2).map(lambda x: (x[0], list(x[1][0]), list(x[1][1]))).collect())

sc.stop()
