#!/usr/bin/env python3
"""
    kv function with two arguments
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Convert a string and a number to a tuple
        and return the square of the number
    """
    return (k, v**2)
