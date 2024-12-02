#!/usr/bin/env python3

"""8-make_multiplier.py"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given float by the multiplier.
    """
    def multiplier_function(n: float) -> float:
        """
        Multiplies the input float by the enclosing multiplier.
        """
        return n * multiplier
    return multiplier_function
