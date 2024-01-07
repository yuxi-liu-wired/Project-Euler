from functools import reduce
import itertools
import math

def natnums():
    return itertools.count(1)


def cumsum(gen):
    return itertools.chain([0], itertools.accumulate(gen))


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


def quotient_remainder(d):
    remainder = 1
    quotient = 0
    while True:
        yield remainder, quotient
        quotient = remainder * 10 // d
        remainder = remainder * 10 % d


def fibonacci():
    fib_tuple = recurrence((0, 1), lambda x: (x[1], x[0] + x[1]))
    return (x[0] for x in fib_tuple)


def tribonacci():
    trib_tuple = recurrence((0, 0, 1), lambda x: (x[1], x[2], x[0] + x[1] + x[2]))
    return (x[0] for x in trib_tuple)


def triangle_numbers():
    return itertools.accumulate(itertools.count(1))


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


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_under_n(n):
    sieves = sieve(n)
    return (i for i in range(n) if sieves[i])


def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, n + 1):
        if sieve[i]:
            sieve[i + i :: i] = [False] * len(sieve[i + i :: i])
    return sieve


def prime_factorization(N):
    primes_gen = primes()
    n = next(primes_gen)
    while N >= n * n:
        while N % n == 0:
            N //= n
            yield n
        n = next(primes_gen)
    if N > 1:
        yield N


def prime_factorization_dict(N):
    prime_factors = {}
    for p in prime_factorization(N):
        prime_factors[p] = prime_factors.get(p, 0) + 1
    return prime_factors


def divisor_count(n):
    d = prime_factorization_dict(n)
    return reduce(lambda x, y: x * (y + 1), d.values(), 1)


def divisor_sum(n):
    d = prime_factorization_dict(n)
    return reduce(lambda x, y: x * (y[0] ** (y[1] + 1) - 1) // (y[0] - 1), d.items(), 1)


def digit_count(n, base=10):
    return math.floor(math.log(n, base)) + 1


def amicable(max_n):
    n = 220
    while n < max_n:
        m = divisor_sum(n) - n
        if n < m and divisor_sum(m) - m == n:
            print(n, m)
            yield n, m
        n += 1


def perfect(max_n):
    n = 1
    while n < max_n:
        if divisor_sum(n) - n == n:
            yield n
        n += 1


def abundant(max_n):
    n = 1
    while n < max_n:
        if divisor_sum(n) - n > n:
            yield n
        n += 1


def deficient(max_n):
    n = 1
    while n < max_n:
        if divisor_sum(n) - n < n:
            yield n
        n += 1


def totient_function(n):
    d = prime_factorization_dict(n)
    for p in d.keys():
        n = n // p * (p - 1)
    return n


def gcd(nums):
    prime_factors = [prime_factorization_dict(n) for n in nums]
    common_factors_dict = {}
    for factors in prime_factors:
        for factor, count in factors.items():
            common_factors_dict[factor] = min(common_factors_dict.get(factor, 0), count)
    return reduce(
        lambda x, y: x * y,
        (factor**count for factor, count in common_factors_dict.items()),
    )


def lcm(nums):
    prime_factors = [prime_factorization_dict(n) for n in nums]
    common_factors_dict = {}
    for factors in prime_factors:
        for factor, count in factors.items():
            common_factors_dict[factor] = max(common_factors_dict.get(factor, 0), count)
    return reduce(
        lambda x, y: x * y,
        (factor**count for factor, count in common_factors_dict.items()),
    )


def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6


def sum_of_first_n(n):
    return n * (n + 1) // 2


def is_pythagorean_triple(a, b, c):
    return a * a + b * b == c * c


def collatz_sequence(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    yield 1


def factorial(k):
    return math.prod(range(1, k + 1))


def base_factorial(n):
    if n == 0:
        return [0]
    k = 1
    while factorial(k) <= n:
        k += 1
    k -= 1
    result = []
    while k > 0:
        f = factorial(k)
        result.append(n // f)
        n %= f
        k -= 1
    return result


def to_base(n, base):
    digits = []
    while n > 0:
        digits.append(n % base)
        n //= base
    return digits[::-1]


def base_factorial_to_permutation(n, p):
    digits = base_factorial(n)
    digits = [0] * (p - 1 - len(digits)) + digits + [0]  # padding in front and back
    L = list(range(p))
    permutation = []
    for digit in digits:
        permutation.append(L.pop(digit))
    return permutation
