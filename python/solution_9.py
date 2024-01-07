from utils.functional import *
import itertools
from math import prod


def stream(n):
    a = 1
    b = 1
    c = n - a - b
    while c >= max(a, b):
        yield (a, b, c)
        if c >= b + 2:
            c -= 1
            b += 1
        else:
            a += 1
            b = a
            c = n - a - b


def answer():
    return prod(next(filter(lambda x: is_pythagorean_triple(*x), stream(1000))))
