# Project Euler 1: Multiples of 3 and 5
from utils.functional import *
import itertools

stream = gen_filter(or_filter(is_multiple_of(3), is_multiple_of(5)), natnums())


def answer(n):
    return sum(itertools.takewhile(lambda x: x < n, stream))
