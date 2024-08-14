#!/usr/bin/env python3
"""sum_mixed_list function with a list of mixed floats and integers"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of a list of mixed floats and integers"""
    sum = 0.0
    for i in range(0, len(mxd_lst)):
        sum += float(mxd_lst[i])
    return sum
