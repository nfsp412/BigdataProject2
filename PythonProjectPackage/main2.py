# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : main2.py
# @Date   : 2023/12/15 19:23
# @Author : sunpeng
# -----------------------------

from pymysql import cursors, Connection

from data_define import Record
from file_define import JsonFileReader

if __name__ == '__main__':
    conn = Connection(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        autocommit=True
    )
    cursor = conn.cursor()

    cursor.execute("select * from py_sql.orders")
    tmp_tuple = cursor.fetchall()
    record_list = []
    for i in tmp_tuple:
        record = Record(i[0], i[1], i[2], i[3])
        print(record, type(i[0]), type(i[1]), type(i[2]), type(i[3]))
        record_list.append(record)

    json_record = JsonFileReader("datas/b.json")
    json_record.write_data(record_list)

    conn.close()
