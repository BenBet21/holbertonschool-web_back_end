#!/usr/bin/env python3
"""
    Simple element_length function with a list of strings
"""

from typing import Iterable, List, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Return a list of tuples
        each tuple containing a string
        and its length
    """
    return [(i, len(i)) for i in lst]
