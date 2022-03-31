# %%
def transfer_zeros(list):
    positiveNum = []
    zero = []
    for number in list:
        if number != 0:
            positiveNum.append(number)
        else:
            zero.append(number)
    positiveNum.extend(zero)
    return positiveNum


list = [3, 4, 0, 2, 0, 5, 1, 6, 2]
print(transfer_zeros(list))
# ----------------------------------------------------------------
# %%


def transfer_zeros(items):
    result = []
    counter = 0
    for item in items:
        if item == 0:
            counter += 1
        else:
            result.append(item)
    result.extend([0] * counter)
    return result
