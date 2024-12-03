#!/usr/bin/env python3

"""
This module provides a function to execute wait_random multiple times
and return the results in sorted order.
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute wait_random n times with max_delay and return sorted results."""
    task = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(task):
        delay = await task
        for i, val in enumerate(delays):
            if delay < val:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)
    return delays
