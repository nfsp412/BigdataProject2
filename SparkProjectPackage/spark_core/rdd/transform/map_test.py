# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : map_test.py
# @Date   : 2023/12/19 22:47
# @Author : sunpeng
# -----------------------------
from typing import Iterable

from pyspark.sql import SparkSession
from pyspark import SparkContext

sc = SparkContext(appName="map", master="local[*]")

rdd = sc.parallelize([1, 2, 3, 4, 5, 6], numSlices=2)


# map 一对一转换,类比select
# res = rdd.map(lambda x: x + 1)


# mapPartitions,传入迭代器传出迭代器,一次性处理一个分区的数据,可以不变增加减少数据,功能丰富,内存有限不推荐使用
def map_partition_func(x: Iterable[int]) -> Iterable[int]:
    l1 = []
    for i in x:
        if i % 2 == 0:
            l1.append(i)

    return iter(l1)


# 使用迭代器函数定义
def map_partition_func_iter(data):
    for i in data:
        if i % 2 == 0:
            yield i


print(rdd.mapPartitions(map_partition_func).collect())
print(rdd.mapPartitions(map_partition_func_iter).collect())


# mapPartitionsWithIndex,额外能获取分区编号,例如获取分区1的数据
def map_partition_index_func(index: [int], x: Iterable[int]):
    l1 = []
    for i in x:
        if index == 1:
            l1.append(i)
    return iter(l1)


print(rdd.mapPartitionsWithIndex(map_partition_index_func).collect())

sc.stop()
