from utils.calendar import day_of_week
import itertools

dates = itertools.product(range(1901, 2001), range(1, 13), [1])


def answer():
    filtered_dates = filter(lambda x: day_of_week(*x) == 0, dates)
    return len(list(filtered_dates))
