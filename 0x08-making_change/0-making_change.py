#!/usr/bin/python3
def makeChange(coins, total):
    count = 0
    coins = sorted(coins)
    while len(coins) > 1:
        coin = coins.pop()
        count += int(total / coin)
        total = total % coin
        if total == 0:
            return count
    return -1