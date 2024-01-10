# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : my_test.py
# @Date   : 2023/12/19 10:43
# @Author : sunpeng
# -----------------------------

from pyspark import SparkContext
import os

os.environ['SPARK_HOME'] = '/opt/module/spark-3.3.2'
os.environ['PYSPARK_HOME'] = '/opt/module/python-3.11.2/bin/python3'

print("Hello World")

sc = SparkContext(master='yarn')
rdd = sc.parallelize([1, 2, 3])
print(rdd.collect())
sc.stop()
