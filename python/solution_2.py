# Project Euler 2: Even Fibonacci numbers
from utils.functional import *
import itertools


def answer():
    n = 4_000_000
    stream = gen_filter(is_multiple_of(2), fibonacci())
    return sum(itertools.takewhile(lambda x: x < n, stream))
