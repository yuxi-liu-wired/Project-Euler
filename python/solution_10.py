from utils.functional import *
import itertools


def answer():
    n = 2_000_000
    return sum(primes_under_n(n))
