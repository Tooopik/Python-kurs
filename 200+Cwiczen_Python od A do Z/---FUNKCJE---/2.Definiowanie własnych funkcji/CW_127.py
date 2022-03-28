# %%
def multi(list):
    result = 1
    for number in list:
        result *= number

    if len(list) > 1:
        return result


print(multi([-4, 6, 2]))

# %%
