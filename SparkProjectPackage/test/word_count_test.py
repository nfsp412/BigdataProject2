# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : word_count_test.py
# @Date   : 2023/12/19 23:16
# @Author : sunpeng
# -----------------------------
import logging

from pyspark import SparkContext

sc = SparkContext(appName="source test", master="local[*]")

rdd = sc.textFile("hdfs://hadoop101:8020/demo.txt")  # 目录嵌套目录,会报错

# word count 1
print("word count 1")
print(rdd.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y).collect())

sc.stop()
