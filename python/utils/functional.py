from functools import reduce


def natnums():
    i = 0
    while True:
        yield i
        i += 1


def cumsum(gen):
    total = 0
    for x in gen:
        yield total
        total += x


def is_multiple_of(n):
    return lambda x: x % n == 0


def and_filter(*args):
    return lambda x: all(f(x) for f in args)


def or_filter(*args):
    return lambda x: any(f(x) for f in args)


def gen_filter(f, gen):
    return (x for x in gen if f(x))


def recurrence(initial, f):
    yield initial
    while True:
        initial = f(initial)
        yield initial


def fibonacci():
    fib_tuple = recurrence((0, 1), lambda x: (x[1], x[0] + x[1]))
    return (x[0] for x in fib_tuple)


def tribonacci():
    trib_tuple = recurrence((0, 0, 1), lambda x: (x[1], x[2], x[0] + x[1] + x[2]))
    return (x[0] for x in trib_tuple)


def primes():
    # The Sieve of Eratosthenes
    primes_so_far = [2]
    yield 2
    while True:
        i = primes_so_far[-1] + 1
        while any(i % p == 0 for p in primes_so_far if p * p <= i):
            i += 1
        primes_so_far.append(i)
        yield i
