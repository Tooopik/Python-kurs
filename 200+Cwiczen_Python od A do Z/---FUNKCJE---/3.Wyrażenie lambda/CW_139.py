# %%
def sort_list(items):
    return sorted(items, key=lambda item: item[1])


a = [(1, 2), (3, 5), (5, 3)]
print(sort_list(a))

# %%
