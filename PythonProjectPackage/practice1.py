# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : practice1.py
# @Date   : 2023/12/16 17:27
# @Author : sunpeng
# -----------------------------

import json
from pyspark import SparkContext, SparkConf
import os

os.environ['PYSPARK_PYTHON'] = 'C:\\Users\\nfsp4\\AppData\\Local\\Programs\\Python\\Python310\\python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("test")
sc = SparkContext(conf=conf)

source_rdd = sc.textFile("C:\\sunpeng\\pythonProject\\search_log.txt")
print(source_rdd.take(1))

cache_rdd = source_rdd.map(lambda x: x.split("\t")).cache()

# 需求1
print(cache_rdd.map(lambda x: (x[0][:2], 1)). \
      reduceByKey(lambda x, y: x + y). \
      sortBy(lambda x: x[1], ascending=False). \
      take(3))

# 需求2
print(cache_rdd.map(lambda x: (x[2], 1)). \
      reduceByKey(lambda x, y: x + y). \
      sortBy(lambda x: x[1], ascending=False). \
      take(3))

# 需求3
print(cache_rdd.filter(lambda x: x[2] == "黑马程序员"). \
      map(lambda x: (x[0][:2], 1)). \
      reduceByKey(lambda x, y: x + y). \
      sortBy(lambda x: x[1], ascending=False). \
      take(1))

# 需求4
source_rdd.map(lambda x: x.split("\t")) \
    .map(lambda x: {"time": x[0], "uid": x[1], "keyword": x[2], "rank1": x[3], "rank2": x[4], "addr": x[5]}) \
    .saveAsTextFile("out")

sc.stop()
