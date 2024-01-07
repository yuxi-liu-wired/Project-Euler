# Project Euler 1: Multiples of 3 and 5
from utils.functional import *
import itertools


def answer():
    n = 1000
    stream = gen_filter(
        or_filter(is_multiple_of(3), is_multiple_of(5)), itertools.count(1)
    )
    return sum(itertools.takewhile(lambda x: x < n, stream))
