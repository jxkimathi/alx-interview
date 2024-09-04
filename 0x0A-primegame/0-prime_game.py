#!/usr/bin/python3
"""Prime Game: Determines the winner after x rounds of a game"""


def sieve_of_eratosthenes(n):
    """Generate list of prime numbers up to n using Sieve of Eratosthenes"""
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


def isWinner(x, nums):
    """Determines the winner after x rounds."""
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    primes_up_to_max = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = 0
        for prime in primes_up_to_max:
            if prime > n:
                break
            primes_count += 1

        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
