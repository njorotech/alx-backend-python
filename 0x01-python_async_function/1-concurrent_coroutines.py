#!/usr/bin/activate
"""Let's execute multiple coroutines at the same time with async"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine that takes in 2 int arguments: n and max_delay"""

    i: int = 0
    delay_list: List[float] = []
    while i < n:
        delay: float = asyncio.create_task(wait_random(max_delay))
        delay_list.append(delay)
        i += 1
    return [await adelay for adelay in asyncio.as_completed(delay_list)]
