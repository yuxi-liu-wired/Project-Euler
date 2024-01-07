from utils.functional import *


# sum of fifth powers of their digits
def answer():
    N = 9**5 * 6
    return sum(n for n in range(2, N) if sum(d**5 for d in to_base(n, 10)) == n)
