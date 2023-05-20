#!/usr/bin/python3
"""Module determins number of coins for total"""


def makeChange(coins, total):
    """Make change function

    Args:
        coins: first integer
        total: second integer

    Returns:
        Total count
    """
    if total <= 0:
        return 0

    count = 0
    coins = sorted(coins)
    while len(coins) > 0:
        coin = coins.pop()
        if coin > total:
            continue
        count += int(total / coin)
        total = total % coin
        if total == 0:
            return count
    return -1
