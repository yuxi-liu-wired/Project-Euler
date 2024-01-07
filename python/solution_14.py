from utils.functional import *
import itertools

n = 1_000_000
collatz_length = {1: 1}
for i in range(2, n):
    x = i
    count = 0
    while x >= i:
        if x % 2 == 0:
            count += 1
            x //= 2
        else:
            count += 1
            x = 3 * x + 1
    collatz_length[i] = count + collatz_length[x]


def answer():
    return max(collatz_length, key=collatz_length.get)
