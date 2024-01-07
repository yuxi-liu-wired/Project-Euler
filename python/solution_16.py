def answer():
    num = int("1" + "0" * 1000, 2)
    return sum(map(int, str(num)))
