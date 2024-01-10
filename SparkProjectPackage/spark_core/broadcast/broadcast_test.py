# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : broadcast_test.py
# @Date   : 2023/12/20 13:47
# @Author : sunpeng
# -----------------------------

from pyspark import SparkContext

sc = SparkContext(appName="broad cast", master="local[*]")

rdd = sc.parallelize([1, 2, 3, 4, 5, 6])

# 设置broadcast广播变量
num = 10
broadcast_var = sc.broadcast(num)

# 使用广播变量
print(rdd.map(lambda x: x + broadcast_var.value).collect())

sc.stop()
