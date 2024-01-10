# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : data_define.py
# @Date   : 2023/12/15 17:50
# @Author : sunpeng
# -----------------------------
from datetime import date


class MyLogDAO(object):
    log_time: str = None
    log_id: str = None
    log_word: str = None
    log_a: int = None
    log_b: int = None
    log_addr: str = None

    def __init__(self, log_time: str, log_id: str, log_word: str, log_a: int, log_b: int, log_addr: str):
        self.log_time = log_time
        self.log_id = log_id
        self.log_word = log_word
        self.log_a = log_a
        self.log_b = log_b
        self.log_addr = log_addr

    def __str__(self):
        return f"log_time: {self.log_time}, log_id: {self.log_id}, log_word: {self.log_word}, log_a: {self.log_a}, log_b: {self.log_b}, log_addr: {self.log_addr}"

    def get_log_time(self):
        return self.log_time

    def get_log_id(self):
        return self.log_id

    def get_log_word(self):
        return self.log_word

    def get_log_addr(self):
        return self.log_addr

    def get_log_a(self):
        return self.log_a

    def get_log_b(self):
        return self.log_b


class Record(object):
    date = None
    order_id = None
    money = None
    province = None

    def __init__(self, date, order_id, money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        """
        {"date": "2011-01-01", "order_id": "c833e851-880f-4e05-9de5-b547f5ffc5e1", "money": 2877, "province": "山东省"}
        :return:
        """
        return "{\"date\": \"" + str(self.date) + "\", \"order_id\": \"" + str(self.order_id) + "\", \"money\": " + str(
            self.money) + ", \"province\": \"" + str(self.province) + "\"}"


if __name__ == '__main__':
    record = Record(date(2023, 12, 15), order_id=1, money=10, province='beijing')
    print(record)
