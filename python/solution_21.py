from math import prod
from utils.functional import *


def amicable(max_n):
    n = 220
    while n < max_n:
        m = divisor_sum(n) - n
        if n < m and divisor_sum(m) - m == n:
            print(n, m)
            yield n, m
        n += 1


def answer():
    n = 10000
    stream = amicable(n)
    numbers_list = list(itertools.chain.from_iterable(stream))
    return sum([x for x in numbers_list if x < n])
