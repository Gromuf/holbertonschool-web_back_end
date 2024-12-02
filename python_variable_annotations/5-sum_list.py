#!/usr/bin/env python3

"""5-sum_list.py"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """list of floats to a sum of floats"""
    res: float = 0
    for i in input_list:
        res += i
    return res
