# Project Euler 2: Even Fibonacci numbers
from utils.functional import *
import itertools


def answer():
    n = 600851475143
    return max(prime_factorization(n))
