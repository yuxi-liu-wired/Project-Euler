from utils.functional import *
import itertools


def quadratic_prime_count(a, b):
    n = 0
    while True:
        N = n**2 + a * n + b
        if not is_prime(N):
            return n
        n += 1


def answer():
    max_count = 0
    max_a = None
    max_b = None
    for a, b in itertools.product(range(-999, 1000), repeat=2):
        count = quadratic_prime_count(a, b)
        if count > max_count:
            max_count = count
            max_a = a
            max_b = b
    return max_a * max_b
