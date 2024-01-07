from utils.functional import *
import itertools

with open("0067_triangle.txt") as f:
    triangle = [[int(x) for x in line.split(" ")] for line in f]

max_triangle = [[0] * len(row) for row in triangle]
max_triangle[0][0] = triangle[0][0]
for i in range(len(triangle)):
    for j in range(len(triangle[i])):
        max_triangle[i][j] = triangle[i][j] + max(
            max_triangle[i - 1][j - 1] if j > 0 else 0,
            max_triangle[i - 1][j] if j < i else 0,
        )


def answer():
    return max(max_triangle[-1])
