def enum(list):
    n = 0
    for i in list:
        yield (n, i)
        n += 1
