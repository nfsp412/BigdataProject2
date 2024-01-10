# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : read_test.py
# @Date   : 2023/12/20 17:38
# @Author : sunpeng
# -----------------------------

from pyspark.sql import SparkSession
import os

# os.environ['SPARK_HOME'] = '/opt/module/spark-3.3.2'
# os.environ['PYSPARK_HOME'] = '/opt/module/python-3.11.2/bin/python3'

spark = SparkSession \
    .builder \
    .config('spark.sql.warehouse.dir', 'hdfs://192.168.10.101:8020/user/hive/warehouse') \
    .config('hive.metastore.uris', 'thrift://192.168.10.101:9083') \
    .enableHiveSupport() \
    .getOrCreate()

# 连接hive
df = spark.sql("show databases")
df.show()

spark.stop()
