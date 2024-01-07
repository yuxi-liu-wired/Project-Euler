from utils.functional import *


def answer():
    nums = base_factorial_to_permutation(1_000_000 - 1, 10)
    return int("".join(str(n) for n in nums))
