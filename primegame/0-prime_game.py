#!/usr/bin/python3

"""
Useless
"""


def is_prime(x):
    """
    Useless comment
    """
    for i in range(2, x):
        if (x % i) == 0:
            return False
    return True


def get_next_prime(numbers):
    """
    Useless comment
    """
    for num in numbers:
        if is_prime(num):
            return num
    return None


def compute_new_list(numbers, last_prime):
    """
    Compute the new list by delete all the multiple of given prime num
    :param numbers: Last list
    :param last_prime: Last prime
    :return: The new list
    """
    numbers = numbers[last_prime - 2:]
    new_numbers = []
    for i in range(len(numbers) - 1):
        if numbers[i] % last_prime != 0:
            new_numbers.append(numbers[i])
    return new_numbers


def isWinner(x, nums):
    """
    Determine the winner
    :param x: The number of game to play
    :param nums: The num limit for each game
    :return:
    """
    first_player_wins = 0
    second_player_wins = 0

    for up_limit in nums:
        numbers = [i for i in range(2, up_limit + 1)]
        steps = 1
        while True:
            num = get_next_prime(numbers)
            if num is None:
                if steps % 2 != 0:
                    second_player_wins += 1
                else:
                    first_player_wins += 1
                break
            numbers = compute_new_list(numbers, num)
            steps += 1

    if first_player_wins > second_player_wins:
        return "Maria"
    if second_player_wins > first_player_wins:
        return "Ben"
    return None
