# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : set_partition_test.py
# @Date   : 2023/12/19 22:27
# @Author : sunpeng
# -----------------------------

from pyspark import SparkContext

sc = SparkContext(appName="source test", master="local[*]")

# 设置分区数量
rdd1 = sc.parallelize([1, 2, 3, 4, 5], numSlices=3)
# 设置分区数量
rdd2 = sc.textFile("hdfs://hadoop101:8020/datas", minPartitions=3)

print(rdd1.glom().collect())
print(rdd2.glom().collect())

sc.stop()
