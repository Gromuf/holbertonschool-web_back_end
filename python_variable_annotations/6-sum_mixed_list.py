#!/usr/bin/env python3

"""6-sum_mixed_list.py"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """list of mixed int and floats to a float"""
    res: float = 0
    for i in mxd_lst:
        res += i
    return res
