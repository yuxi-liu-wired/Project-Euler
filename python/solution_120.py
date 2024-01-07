# Idea of solution: By binomial theorem, and simplifying, we have
# $$
# (a-1)^n + (a+1)^n \equiv 2na \pmod{a^2}
# $$
# if $n$ is odd. If $n$ is even, it is just $2$, which is smaller. Now simplify.


def r_max(a):
    assert a >= 3
    if a % 2 == 0:
        return a * (a - 2)
    else:
        return a * (a - 1)


sum(map(r_max, range(3, 1001)))
