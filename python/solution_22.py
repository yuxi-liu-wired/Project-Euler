with open("0022_names.txt") as f:
    names = f.read().split(",")
names = [x[1:-1].upper() for x in names]
names = sorted(names)


def sum_of_letters(string):
    return sum(map(lambda x: ord(x) - 64, string))


def answer():
    return sum((i + 1) * sum_of_letters(name) for i, name in enumerate(names))
