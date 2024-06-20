#!/usr/bin/python3
"""make change methods"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    fewest number of coins needed to meet total
    Args:
        coins <List[int]>: list of the values coins.
        total <int>: total number.
    Return <int>:
        The minimum number of coins.
    """
    if total <= 0:
        return 0
    count = 0
    coins.sort(reverse=True)
    for coin in coins:
        while coin <= total:
            total -= coin
            count += 1
    return count if not total else -1
