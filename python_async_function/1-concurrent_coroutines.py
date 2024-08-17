#!/usr/bin/env python3
"""
Import wait_random from the previous Python file
and write an asynchronous function called wait_n
that takes two integer arguments: n and max_delay.
The function should call wait_random n times
with the given max_delay and return
a list of all the delays (as floats)
in ascending order, without using sort()
due to concurrency.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Launch wait_random n times using the given max_delay"""
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted (delays)
