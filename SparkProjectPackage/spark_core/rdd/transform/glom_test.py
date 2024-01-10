# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : glom_test.py
# @Date   : 2023/12/20 9:47
# @Author : sunpeng
# -----------------------------


from pyspark import SparkContext

sc = SparkContext(appName="map", master="local[*]")

rdd = sc.parallelize([1, 2, 3, 4, 5, 6], numSlices=2)

# 指的是将同一个分区的数据转换成相同类型的内存数组,可以用来查看分区效果
# 例如分区内求最大值,分区间求和
res = (rdd.glom().map(lambda x: max(x)).reduce(lambda x, y: x + y))

print(res)

sc.stop()
