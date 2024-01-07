from math import prod
from utils.functional import *
import itertools


def answer():
    n = 28_123
    abundant_nums = list(abundant(n))
    stream = itertools.combinations_with_replacement(abundant_nums, 2)
    sum_stream = map(sum, stream)
    return sum(set(range(1, n + 1)) - set(sum_stream))
