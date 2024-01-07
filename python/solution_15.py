from utils.functional import *
import itertools

n = 20 + 1
array = [[0 for _ in range(n)] for _ in range(n)]
array[0][0] = 1
for i in range(n):
    for j in range(n):
        array[i][j] += (array[i - 1][j] if i > 0 else 0) + (
            array[i][j - 1] if j > 0 else 0
        )


def answer():
    return array[n - 1][n - 1]
