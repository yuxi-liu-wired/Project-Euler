from utils.functional import *
import itertools


def answer():
    n = 1_000_000
    primes = list(primes_under_n(n))
    prime_sums = [0] + list(itertools.accumulate(primes))
    best_length = 21
    best_prime = 0
    while prime_sums[best_length] < n:
        for i in range(len(primes) - best_length):
            total = prime_sums[i + best_length] - prime_sums[i]
            if total > n:
                break
            if total < n and is_prime(total):
                best_prime = total
                best_length_found = best_length
                break
        best_length += 1
    return best_prime
