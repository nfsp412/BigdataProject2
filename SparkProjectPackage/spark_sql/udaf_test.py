# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : udf_test.py
# @Date   : 2023/12/20 23:09
# @Author : sunpeng
# -----------------------------
from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, IntegerType, StringType
from pyspark.sql import functions as F

spark = SparkSession.builder.getOrCreate()

r1 = Row(id=1001, name="张三", age=20)
r2 = Row(id=1002, name="李四", age=23)
schema_type = StructType() \
    .add("id", IntegerType(), False) \
    .add("name", StringType(), True) \
    .add("age", IntegerType(), True)
df = spark.createDataFrame([r1, r2], schema_type)
df.show()
df.printSchema()


# 使用内置函数的装饰器的方式定义UDF函数,无需再注册,直接在DSL中使用
@F.udf(StringType())
def my_udf(x):
    return "Name: " + x


# 使用自定义UDF
# 在DSL使用UDF
df.select(my_udf("name")).show()

spark.stop()
