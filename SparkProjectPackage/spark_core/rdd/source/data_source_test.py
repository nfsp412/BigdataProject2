# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : data_source_test.py
# @Date   : 2023/12/19 22:16
# @Author : sunpeng
# -----------------------------

from pyspark import SparkContext

sc = SparkContext(appName="source test", master="local[*]")

rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize({"name": "zs", "age": 18})  # 字典数据只转换了key
# 使用列表嵌套元组
rdd_tuple = sc.parallelize([("name", "zs"), ("age", 18)])
rdd3 = sc.parallelize({1, 2, 3})

print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())

print(rdd_tuple.collect())

sc.stop()
