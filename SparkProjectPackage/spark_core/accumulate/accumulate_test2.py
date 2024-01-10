# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : accumulate_test.py
# @Date   : 2023/12/20 13:50
# @Author : sunpeng
# -----------------------------

from pyspark import SparkContext, Accumulator
from pyspark.accumulators import T, AccumulatorParam
from MyAccumulate import MyAccumulate

sc = SparkContext(appName="accumulate", master="local[*]")

rdd = sc.parallelize([1, 2, 3, 4, 5, 6], numSlices=2)

# 定义累加器
accu_var = sc.accumulator(value={"sum": 0, "count": 0}, accum_param=MyAccumulate())

# 使用累加器
rdd.foreach(lambda x: accu_var.add({"sum": x, "count": 1}))

# 查看累加器的结果
print(accu_var.value)

sc.stop()
