#!/usr/bin/env python3
"""This modudle contains asynchronous coroutine
function that takes in an integer argument.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This coroutine waits for a random number of seconds.
    """

    wait_period = random.random() * max_delay
    await asyncio.sleep(wait_period)
    return wait_period
