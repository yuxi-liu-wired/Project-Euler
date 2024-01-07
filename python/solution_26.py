from utils.functional import *
import itertools


def repeat_cycle_length(d, print_digits=False):
    stream = quotient_remainder(d)
    qr_set = {}
    qr_list = []
    i = 0
    while True:
        qr = next(stream)
        qr_list.append(qr)
        if qr in qr_set.keys():
            qr_list = [str(x[1]) for x in qr_list]
            head_digits = qr_list[1 : qr_set[qr]]
            repeating_digits = qr_list[qr_set[qr] : -1]
            if print_digits:
                print(
                    f"0.{''.join(head_digits)}\x1b[6;30;42m{''.join(repeating_digits)}\x1b[0m"
                )
            return i - qr_set[qr]
        qr_set[qr] = i
        i += 1


def answer():
    max_d = 2
    max_cycle_length = 0
    for i in range(2, 1000):
        cycle_length = repeat_cycle_length(i, print_digits=False)
        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
            max_d = i
    return max_d
