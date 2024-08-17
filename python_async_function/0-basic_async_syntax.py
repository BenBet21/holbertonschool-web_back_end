#!/usr/bin/env python3
"""
Write an asynchronous coroutine named
wait_random that takes an integer argument
max_delay (defaulting to 10). It should
wait for a random delay between
0 and max_delay seconds
(inclusive, as a float) and then return it.
Use the random module.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
