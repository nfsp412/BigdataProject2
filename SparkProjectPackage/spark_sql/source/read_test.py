# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : read_test.py
# @Date   : 2023/12/20 17:38
# @Author : sunpeng
# -----------------------------

from pyspark.sql import SparkSession
import os

os.environ['SPARK_HOME'] = '/opt/module/spark-3.3.2'
os.environ['PYSPARK_HOME'] = '/opt/module/python-3.11.2/bin/python3'

spark = SparkSession \
    .builder \
    .appName("Python Spark") \
    .master("local[*]") \
    .getOrCreate()

# # 读取json
# df = spark.read.format("json").option("multiline", True).load("C:\\sunpeng\\pythonSpark\\data.json")
# df.show()
# df.printSchema()
#
# # 读取csv
# df1 = spark.read.csv("C:\\sunpeng\\pythonSpark\\data.csv", header=True)
# df1.show()
# df1.printSchema()
#
# # 读取文本文件指定分隔符
# df2 = spark.read.csv("C:\\sunpeng\\pythonSpark\\data.txt", header=True, sep=";")
# df2.show()
# df2.printSchema()

# 读取MySQL
url = "jdbc:postgresql://192.168.10.103:5432/postgres?characterEncoding=UTF-8"
table_name = "tb1"
properties = {
    "user": "postgres",
    "password": "123456",
    "driver": "org.postgresql.Driver"
}
df3 = spark.read.jdbc(url=url, table=table_name, properties=properties)
df3.show()
df3.printSchema()

spark.stop()
