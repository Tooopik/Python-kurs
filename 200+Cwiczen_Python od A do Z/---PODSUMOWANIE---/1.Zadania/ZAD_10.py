# %%
def identity(number):
    result = []
    x = []
    idx = 0
    while idx < number:
        while len(x) < number:
            x.append(0)
        x[idx] = 1
        result.append(x)
        x = []
        idx += 1
    return result


print(identity(4))

# %%


def identity(n):
    array = [[0]*n for i in range(n)]
    for idx, item in enumerate(array):
        item[idx] = 1
    return array
