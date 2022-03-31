# %%
def concat(list1, list2):
    result = []
    list1 = [item[0] for item in list1]
    list2 = [item[0] for item in list2]
    idx = 0
    for item in list1:
        result.append([item, list2[idx]])
        idx += 1
    return result


l1 = [[1], [2]]
l2 = [[3], [4]]

print(concat(l1, l2))

# %%


def concat(l1, l2):
    result = []
    for i, j in zip(l1, l2):
        result.append([i[0], j[0]])
    return result
