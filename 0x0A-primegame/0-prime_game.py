#!/usr/bin/python3
"""methods found winner isWinner"""


def primesNumberOf(num):
    """method that return all prime number between two to num
        based on algorithm of Sieve of Eratosthenes.

    Args:
        num (int): max integer of prime number.

    Return:
        list of prime number 2, ... num.
    """
    checker = [True] * (num + 1)
    start = 2
    while (start * start <= num):
        if checker[start]:
            for i in range(start * start, num + 1, start):
                checker[i] = False
        start += 1
    return [n for n in range(2, num + 1) if checker[n]]


def isWinner(x, nums):
    """Return winner based on x and nums"""
    if not x or not nums:
        return None

    maria = ben = 0
    for index in range(x):
        primesNumber = primesNumberOf(nums[index])
        if len(primesNumber) % 2:
            maria += 1
        else:
            ben += 1
    return None if maria == ben else 'Maria' if maria > ben else 'Ben'
