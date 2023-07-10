#!/usr/bin/env python3

"""This module executes multiple coroutines
at the same time with async.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This coroutine function executes wait_random n times
    """
    wait_periods = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n))))
    return sorted(wait_periods)
