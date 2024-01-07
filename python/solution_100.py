from utils.functional import *
import itertools


# Idea of solution:
# $$
# 2 b(b-1)  = (b+r) (b+r-1)
# $$

# Let $c = b+r$, then we have
# $$
# (2c-1)^2 + 1 = 2(2b-1)^2
# $$

# Let $x = 2c-1 = 2b+2r-1, y = 2b-1$, we have the Pell equation form $x^2-2y^2=-1$.
# which has a certain recurrence relation.


def generate_pell_solutions(limit):
    x, y = 1, 1
    while x < limit:
        yield x, y
        x, y = x + 2 * y, x + y
        x, y = x + 2 * y, x + y


def generate_blue_red(limit):
    return (
        ((y + 1) // 2, (x - y) // 2)
        for x, y in generate_pell_solutions(limit)
        if (y + 1) % 2 == 0 and (x - y) % 2 == 0
    )


def answer():
    n = 10**12
    stream = itertools.dropwhile(lambda x: x[0] + x[1] < n, generate_blue_red(n * 10))
    return next(stream)[0]
