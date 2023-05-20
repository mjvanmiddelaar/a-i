#!/usr/bin/python3
def makeChange(coins, total):
    """make change
    """
    count = 0
    coins = sorted(coins)
    while True:
        coin = coins.pop()
        count += int(total / coin)
        total = total % coin
        if total == 0:
            return count
        if len(coins) == 1:
            break
    return -1