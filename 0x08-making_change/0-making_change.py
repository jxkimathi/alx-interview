#!/usr/bin/python3
"""Making change interview question"""


def makeChange(coins, total):
    """Find the fewest number of coins needed to meet a given amount"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    number_coins = 0
    for coin in coins:
        if total <= 0:
            break
        number_coins += total // coin
        total = total % coin
    return number_coins
