# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : file_define.py
# @Date   : 2023/12/15 17:53
# @Author : sunpeng
# -----------------------------
import json

from data_define import Record


class FileReader(object):
    def read_data(self) -> list[Record]:
        pass

    def write_data(self, data: list[Record]) -> None:
        pass


class TextFileReader(FileReader):
    path = None

    def __init__(self, path):
        self.path = path

    def write_data(self, data: list[Record]) -> None:
        f = None
        try:
            f = open(self.path, 'w', encoding='utf-8')
            for i in data:
                # tmp_dict = {"date": i.date, "order_id": i.order_id, "money": i.money, "province": i.province}
                # f.write(str(tmp_dict))
                f.write(str(i))
        except Exception as e:
            print(e)
        finally:
            if f:
                f.close()

    def read_data(self):
        f = None
        record_list = []
        try:
            f = open(self.path, 'r', encoding='utf-8')
            for i in f.readlines():
                tmp_list = i.strip().split(",")
                record = Record(tmp_list[0], tmp_list[1], float(tmp_list[2]), tmp_list[3])
                record_list.append(record)
        except Exception as e:
            print(f"异常{e}")
        finally:
            if f:
                f.close()
        return record_list


class JsonFileReader(FileReader):
    path = None

    def __init__(self, path):
        self.path = path

    def write_data(self, data: list[Record]) -> None:
        f = None
        try:
            f = open(self.path, 'w', encoding='utf-8')
            for i in data:
                tmp_dict = {"date": str(i.date), "order_id": str(i.order_id), "money": str(i.money),
                            "province": str(i.province)}
                tmp_str = json.dumps(tmp_dict, ensure_ascii=False)
                f.write(tmp_str)
                f.write("\n")
        except Exception as e:
            print(f"异常{e}")
        finally:
            if f:
                f.close()

    def read_data(self) -> list[Record]:
        f = None
        record_list = []
        try:
            f = open(self.path, 'r', encoding='utf-8')
            for i in f:
                tmp_dict = json.loads(i)
                record = Record(tmp_dict['date'], tmp_dict['order_id'], float(tmp_dict['money']),
                                tmp_dict['province'])
                record_list.append(record)
        except Exception as e:
            print(f"异常{e}")
        finally:
            if f:
                f.close()
        return record_list


if __name__ == '__main__':
    record = Record("2011-01-01", "c833e851-880f-4e05-9de5-b547f5ffc5e1", 2877, "山东省")
    record_list = [record]
    reader = TextFileReader("datas/a.txt")
    reader.write_data(record_list)

    reader_json = JsonFileReader("datas/a.json")
    reader_json.write_data(record_list)

    # reader = TextFileReader("C:\\sunpeng\\pythonProject\\2011年1月销售数据.txt")
    # text_list = reader.read_data()
    # for i in text_list:
    #     print(i)
    #
    # reader_json = JsonFileReader("C:\\sunpeng\\pythonProject\\2011年2月销售数据JSON.txt")
    # json_list = reader_json.read_data()
    # for i in json_list:
    #     print(i)
