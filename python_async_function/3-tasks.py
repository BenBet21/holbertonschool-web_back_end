#!/usr/bin/env python3
"""
Write a regular function called task_wait_random
that takes an integer max_delay as an argument
and returns an asyncio.Task.
"""

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """return asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
