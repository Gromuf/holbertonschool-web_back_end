#!/usr/bin/env python3

"""
This module measures the runtime of the wait_n coroutine
and calculates the average execution time per call.
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of wait_n
    and return the average time per call.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    temps = end_time - start_time
    return temps / n
