from utils.functional import *
import itertools


def answer():
    n = 10_001
    return list(itertools.islice(primes(), n - 1, n))[0]
