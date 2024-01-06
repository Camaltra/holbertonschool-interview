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
        if is_prime(num) and num != 1:
            return num
    return None


def compute_new_list(numbers, last_prime):
    """
    Compute the new list by delete all the multiple of given prime num
    :param numbers: Last list
    :param last_prime: Last prime
    :return: The new list
    """
    new_numbers = []
    for i in range(len(numbers)):
        if numbers[i] % last_prime != 0:

            new_numbers.append(numbers[i])
        print(numbers[i], last_prime)
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

    if x <= 0 or x > len(nums):
        return None

    for ix_party in range(x):
        if nums[ix_party] == 1:
            continue
        numbers = [i for i in range(1, nums[ix_party] + 1)]
        steps = 1
        while True:
            print(numbers)
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
