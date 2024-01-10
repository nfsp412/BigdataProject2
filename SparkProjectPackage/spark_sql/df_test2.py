# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : spark_session_test.py
# @Date   : 2023/12/20 16:06
# @Author : sunpeng
# -----------------------------

from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, IntegerType, StringType

spark = SparkSession \
    .builder \
    .appName("Python Spark") \
    .master("local[*]") \
    .getOrCreate()

# 生成RDD
sc = spark.sparkContext
rdd = sc.parallelize([(1001, "张三", 20), (1002, "李四", 22), (1003, "王五", 18)])

# 定义Schema
schema_type = StructType() \
    .add("id", IntegerType(), False) \
    .add("name", StringType(), True) \
    .add("age", IntegerType(), True)

# RDD转换成DF
df = rdd.toDF(schema_type)

# 查看
df.show()
df.printSchema()

spark.stop()
