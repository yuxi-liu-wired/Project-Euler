from utils.functional import *
import itertools


def answer():
    n = 500
    return next(
        itertools.dropwhile(lambda x: divisor_count(x) < 500, triangle_numbers())
    )
