from utils.functional import *
import itertools


def answer():
    factorizations = set()
    for a in range(2, 101):
        fact = prime_factorization_dict(a)
        for b in range(2, 101):
            new_fact = {(p, (b * e)) for p, e in fact.items()}
            factorizations.add(frozenset(new_fact))
    return len(factorizations)
