# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : glom_test.py
# @Date   : 2023/12/20 9:47
# @Author : sunpeng
# -----------------------------


from pyspark import SparkContext

sc = SparkContext(appName="map", master="local[*]")

rdd = sc.parallelize([1, 2, 3, 4, 5, 6], numSlices=4)

# coalesce算子减少分区,存在过多小任务时使用
print(rdd.coalesce(1).collect())
# repartition增大分区,底层还是coalesce,shuffle=True参数
# rdd.repartition()

sc.stop()
