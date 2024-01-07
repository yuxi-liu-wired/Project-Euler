# Project Euler 2: Even Fibonacci numbers
from utils.functional import *
import itertools


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def descending_stream(min_n, max_n):
    for sum in range(max_n * 2, min_n * 2 - 1, -1):
        for diff in range(0, sum // 2):
            x = (sum + diff) // 2
            y = (sum - diff) // 2
            if x > max_n or y < min_n:
                continue
            yield (x, y)


def answer():
    stream = (x * y for x, y in descending_stream(100, 999) if is_palindrome(x * y))
    return list(itertools.islice(stream, 1))[0]
