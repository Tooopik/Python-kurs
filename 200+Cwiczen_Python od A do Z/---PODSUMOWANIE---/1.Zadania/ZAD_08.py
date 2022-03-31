# %%
def arange(start=1, stop=10, step=1):
    result = []
    number = start
    while number <= stop:
        result.append(number)
        number += step
    return result


print(arange(1, 10000000))

# %%


def arange(start, stop, step=1):
    result = []
    for i in range(start, stop, step):
        result.append(i)
    return result
