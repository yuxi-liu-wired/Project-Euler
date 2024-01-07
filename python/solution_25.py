from utils.functional import *
import itertools


def answer():
    stream = zip(itertools.count(0), fibonacci())
    filtered_stream = (i for i, f in stream if len(str(f)) == 1000)
    return next(filtered_stream)
