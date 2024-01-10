# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : MyAccumulate.py
# @Date   : 2023/12/20 14:09
# @Author : sunpeng
# -----------------------------
from typing import Tuple, Callable

from pyspark import AccumulatorParam
from pyspark.accumulators import T, Accumulator


class MyAccumulate(AccumulatorParam):
    def zero(self, value: dict[str, int]) -> dict[str, int]:
        return value

    def addInPlace(self, value1: dict[str, int], value2: dict[str, int]) -> dict[str, int]:
        for k, v in value2.items():
            value1[k] += v
        return value1
