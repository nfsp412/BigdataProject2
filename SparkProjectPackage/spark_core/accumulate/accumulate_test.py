# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : accumulate_test.py
# @Date   : 2023/12/20 13:50
# @Author : sunpeng
# -----------------------------

from pyspark import SparkContext

sc = SparkContext(appName="accumulate", master="local[*]")

rdd = sc.parallelize([1, 2, 3, 4, 5, 6])

# 定义累加器
num = 0
accu_var = sc.accumulator(num)

# 使用累加器
print(rdd.map(lambda x: accu_var.add(1)).collect())

# 查看累加器的结果
print(accu_var.value)

sc.stop()

