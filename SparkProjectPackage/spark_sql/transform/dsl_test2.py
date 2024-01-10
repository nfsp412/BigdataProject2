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
r1 = Row(1001, "张三", 20, '2023-11-26', '1703077252')
r2 = Row(id=1002, name="李四", age=23, dt='2023-11-24', ut='1703077252')
r3 = Row(id=1003, name="王五", age=18, dt='2023-11-25', ut='1703077252')
# 再创建Schema
schema_type = StructType() \
    .add("id", IntegerType(), False) \
    .add("name", StringType(), True) \
    .add("age", IntegerType(), True) \
    .add("dt", StringType(), True) \
    .add("ut", StringType(), True)
# 最后创建DF
df = spark.createDataFrame([r1, r2, r3], schema_type)
# 查看
df.show()
# 查看schema信息
df.printSchema()

# DSL内置函数
from pyspark.sql import functions as F

# 字符串函数
df.select(F.concat('name', 'age')).show()
df.select(F.concat_ws('-', 'name', 'age')).show()
df.select(F.substring('id', 1, 2)).show()
df.select(F.split("dt", "-")).show()
# 时间日期
df.select(F.current_date()).show()
df.select(F.unix_timestamp()).show()
df.select(F.current_timestamp()).show()
df.select(F.from_unixtime("ut", format="yyyyMMdd")).show()
df.select(F.date_add("dt", 1)).show()
# 聚合处理
df.groupBy("id").agg(F.sum("age"), F.count("age")).show()

spark.stop()
