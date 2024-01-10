# # -*- coding: utf-8 -*
# # -----------------------------
# # @Project: pythonProject
# # @File   : test29.py
# # @Date   : 2023/12/15 21:27
# # @Author : sunpeng
# # -----------------------------
#
# """
# pyspark
# """
# import json
#
# from pyspark import SparkContext, SparkConf
#
# # 解决报错
# import os
#
# os.environ['PYSPARK_PYTHON'] = 'C:\\Users\\nfsp4\\AppData\\Local\\Programs\\Python\\Python310\\python.exe'
#
# conf = SparkConf().setMaster("local[*]").setAppName("test")
# sc = SparkContext(conf=conf)
#
# print(sc.version)
#
# # 字典的key,字符串拆分成单个字符
# # rdd = sc.parallelize([1, 2, 3, 4, 5])
# # print(rdd.collect())
#
# # rdd = sc.textFile("hello.txt")
# # print(rdd.collect())
#
# # rdd1 = rdd.map(lambda x: x * 2).collect()
# # print(rdd1)
#
# # flatmap
# # rdd = sc.parallelize(["1 2 3", "4", "5 6"])
# # print(rdd.flatMap(lambda line: line.split(" ")).collect())
#
# # rdd = sc.parallelize([[1, 2, 3], [4], [5, 6]])
#
#
# # def f1(x: list[list[int]]) -> list[int]:
# #     l1 = []
# #     for i in x:
# #         # print(i)
# #         if isinstance(i, list):
# #             for j in i:
# #                 l1.append(j)
# #         else:
# #             l1.append(i)
# #     return l1
#
#
# # print(rdd.flatMap(f1).collect())
#
# # reduceByKey
# # rdd = sc.parallelize([('a', 1), ('a', 1), ('b', 1)])
# # print(rdd.reduceByKey(lambda x, y: x + y).collect())
#
# # wordcount
# # rdd = sc.textFile("word")
# # rdd1 = rdd.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
#
# # filter
# # rdd = sc.parallelize([1, 2, 3, 4, 5])
# # print(rdd.filter(lambda x: x % 2 == 0).collect())
#
# # rdd = sc.parallelize([1, 2, 2, 3])
# # print(rdd.distinct().collect())
#
# # print(rdd1.sortBy(lambda x: x[1], ascending=False, numPartitions=1).collect())
#
# # 案例1
# # rdd = sc.textFile("file1")
#
# # print(rdd.flatMap(lambda x: x.split("|")).map(lambda x: json.loads(x)).collect())
# # rdd1 = rdd.flatMap(lambda x: x.split("|")).map(lambda x: json.loads(x)).cache()
#
# # 销售额
# # print(rdd1.map(lambda x: type(x)).collect())
# # print(rdd1.map(lambda x: (str(x["areaName"]), int(x["money"]))).reduceByKey(lambda x, y: x + y).sortBy(lambda x: x[1],
# # ascending = False,
# # numPartitions = 1).collect())
#
# # 需求2
# # print(rdd1.map(lambda x: (x["areaName"], x["category"])).distinct().collect())
#
# # 需求3
# # print(rdd1.filter(lambda x: x["areaName"] == "北京").map(lambda x: (x["category"], x["areaName"])).distinct().collect())
#
# #
# # rdd = sc.parallelize(range(1, 10))
# # print(rdd.collect())
#
# # print(rdd.reduce(lambda x, y: x + y))
#
# # rdd = sc.parallelize(range(10),numSlices=1)
# # print(rdd.collect())
# # print(rdd.take(3))
# # print(rdd.count())
#
# # 该路径是目录
# # rdd.saveAsTextFile("20231216")
#
# rdd = sc.textFile("C:\\sunpeng\\pythonProject\\search_log.txt")
# print(rdd.take(10))
#
# from data_define import MyLogDAO
#
#
# def my_map_func1(x: str):
#     l1 = x.split("\t")
#     return MyLogDAO(l1[0], l1[1], l1[2], int(l1[3]), int(l1[4]), l1[5])
#
#
# rdd2 = rdd.map(my_map_func1).cache()
# print(rdd2.take(10))
#
#
# # 需求1
# def f2(x) -> tuple[str, int]:
#     tmp_str: str = x.get_log_time
#     return (tmp_str.split(":")[0], 1)
#
#
# print(rdd2.map(f2).reduceByKey(lambda x, y: x + y).collect())
#
# sc.stop()
