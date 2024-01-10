# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : set_partition_test.py
# @Date   : 2023/12/19 22:27
# @Author : sunpeng
# -----------------------------

from pyspark import SparkContext

sc = SparkContext(appName="source test", master="yarn")

# 读取小文件,进行合并
rdd1 = sc.wholeTextFiles("hdfs://hadoop101:8020/datas2")

print(rdd1.glom().collect())

sc.stop()
