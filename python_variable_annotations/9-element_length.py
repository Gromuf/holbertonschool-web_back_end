#!/usr/bin/env python3

"""9-element_length.py"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each element in the given iterable of sequences.
    """
    return [(i, len(i)) for i in lst]
