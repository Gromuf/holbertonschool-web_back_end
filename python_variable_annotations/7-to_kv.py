#!/usr/bin/env python3

"""7-to_kv.py"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """k and v to a tuple (k,v*v)"""
    return (k, v * v)
