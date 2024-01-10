# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : data_source_test.py
# @Date   : 2023/12/19 22:16
# @Author : sunpeng
# -----------------------------

from pyspark import SparkContext

sc = SparkContext(appName="source test", master="local[*]")

# rdd = sc.textFile("C:\\sunpeng\\pythonSpark\\demo.txt")
# rdd = sc.textFile("hdfs://hadoop101:8020/demo.txt")
# 读取目录
rdd = sc.textFile("hdfs://hadoop101:8020/datas")  # 目录嵌套目录,会报错

print(rdd.collect())

sc.stop()
