# %%
def count_str(list):
    result = []
    for object in list:
        if isinstance(object, str) and len(object) > 2:
            result.append(object)
    return len(result)


print(count_str([1, 'xoxo', 'Python', True]))

# %%
