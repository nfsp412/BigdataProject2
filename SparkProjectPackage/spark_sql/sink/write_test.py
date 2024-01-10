# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : write_test.py
# @Date   : 2023/12/20 21:27
# @Author : sunpeng
# -----------------------------
from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, IntegerType, StringType
import os

os.environ['SPARK_HOME'] = '/opt/module/spark-3.3.2'
os.environ['PYSPARK_HOME'] = '/opt/module/python-3.11.2/bin/python3'
os.environ['YARN_CONF_DIR'] = '/opt/module/hadoop-3.1.3/etc/hadoop/'

spark = SparkSession \
    .builder \
    .appName("Python Spark") \
    .master("local[*]") \
    .config("org.spark.sql.shuffle.partitions", "1") \
    .getOrCreate()

r1 = Row(id=1001, name="张三", age=20)
r2 = Row(id=1002, name="李四", age=23)
r3 = Row(id=1003, name="王五", age=18)
schema_type = StructType() \
    .add("id", IntegerType(), False) \
    .add("name", StringType(), True) \
    .add("age", IntegerType(), True)
df = spark.createDataFrame([r1, r2, r3], schema_type)
df.show()
df.printSchema()

# write
# 写入json
df.write.json("hdfs:///pyspark/data.json", mode="overwrite")
# 写入csv
df.write.csv("hdfs:///pyspark/data.csv", mode="overwrite")
# 写入MySQL
url = "jdbc:postgresql://192.168.10.103:5432/postgres?characterEncoding=UTF-8"
table_name = "tb2"
properties = {
    "user": "postgres",
    "password": "123456",
    "driver": "org.postgresql.Driver"
}
df.write.jdbc(url=url, table=table_name, properties=properties)

spark.stop()
