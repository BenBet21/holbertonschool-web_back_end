#!/usr/bin/env python3
"""
Modify the wait_n function to create a new function
called task_wait_n.
The code should be almost identical,
but instead of calling wait_random,
it should call task_wait_random.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Launch task_wait_random n times using the given max_delay"""
    delays = [await task_wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
