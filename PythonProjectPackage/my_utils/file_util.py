# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : file_util.py
# @Date   : 2023/12/15 10:35
# @Author : sunpeng
# -----------------------------

def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, 'r', encoding='utf-8')
        for i in f:
            print(i)
    except Exception as e:
        print(f"异常{e}")
    finally:
        if f:
            f.close()


def append_to_file(file_name, content):
    f = None
    try:
        f = open(file_name, 'a', encoding="utf-8")
        f.write(content)
    except Exception as e:
        print(f"异常{e}")
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    print_file_info("../datas/1.txt")
    append_to_file("../datas/1.txt", "ABCDE")
    print_file_info("../datas/1.txt")
