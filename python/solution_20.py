from math import prod


def answer():
    num = prod(range(1, 101))
    return sum(map(int, str(num)))
