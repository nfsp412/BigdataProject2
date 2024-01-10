# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : main1.py
# @Date   : 2023/12/15 17:49
# @Author : sunpeng
# -----------------------------
from file_define import TextFileReader, JsonFileReader
from pymysql import cursors, Connection

if __name__ == '__main__':
    reader = TextFileReader("C:\\sunpeng\\pythonProject\\2011年1月销售数据.txt")
    text_list = reader.read_data()

    reader_json = JsonFileReader("C:\\sunpeng\\pythonProject\\2011年2月销售数据JSON.txt")
    json_list = reader_json.read_data()

    # 合并两个list
    list1 = json_list + text_list

    conn = Connection(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        autocommit=True
    )
    cursor = conn.cursor()
    for i in list1:
        cursor.execute("insert into py_sql.orders (order_date, order_id, money, province) values (%s, %s, %s, %s)", (
            i.date, i.order_id, i.money, i.province
        ))

    conn.close()
