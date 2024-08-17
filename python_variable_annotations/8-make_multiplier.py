#!/usr/bin/env python3
"""make_multiplier function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Return a function that multiplies
    """
    def multi(n: float) -> float:
        """
            Return the product of n and multiplier
        """
        return n * multiplier
    return multi
