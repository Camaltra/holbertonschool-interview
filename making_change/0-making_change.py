#!/usr/bin/pythton

"""
Useless
"""

def makeChange(coins, total):
    """
    Make the change
    :param coins: The coins uvailable
    :param total: The total to reach
    :return: -1 or the number of step
    """
    if total <= 0:
        return 0

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]
