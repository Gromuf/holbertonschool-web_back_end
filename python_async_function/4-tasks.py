#!/usr/bin/env python3

"""4-tasks.py"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute wait_random n times with max_delay and return sorted results."""
    task = [task_wait_random(max_delay) for _ in range(n)]
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
