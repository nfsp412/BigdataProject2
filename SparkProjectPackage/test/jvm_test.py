# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : jvm_test.py
# @Date   : 2023/12/20 19:56
# @Author : sunpeng
# -----------------------------
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.column import _to_java_column

spark = SparkSession \
    .builder \
    .appName("xml") \
    .master("local[*]") \
    .getOrCreate()

java_col = _to_java_column("name")
print(type(java_col))
print(java_col)

var = spark._jsparkSession
print(type(var))
print(var)

jvm = spark._jvm
print(type(jvm))
print(jvm)

a = jvm.com.databricks.spark.xml
print(type(a))
print(a)

spark.stop()
