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

# 直接创建DF
# 先创建Row
r1 = Row(1001, "张三", 20)
r2 = Row(id=1002, name="李四", age=23)
# 再创建Schema
schema_type = StructType() \
    .add("id", IntegerType(), False) \
    .add("name", StringType(), True) \
    .add("age", IntegerType(), True)
# 最后创建DF
df = spark.createDataFrame([r1, r2], schema_type)
# 查看
df.show()
# 查看schema信息
df.printSchema()

spark.stop()
