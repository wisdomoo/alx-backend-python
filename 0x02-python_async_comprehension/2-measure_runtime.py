#!/usr/bin/env python3

"""Task 2-s module
"""

import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This coroutine executes async_comprehension 4 times in
    parallel using asyncio.gather and measures the total execution
    Time.
    """

    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.time() - start_time
