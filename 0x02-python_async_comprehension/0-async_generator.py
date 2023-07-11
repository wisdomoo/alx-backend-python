#!/usr/bin/env python3

"""Task 0's module
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """This coroutine generates a sequence of 10 Numbers.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 1
