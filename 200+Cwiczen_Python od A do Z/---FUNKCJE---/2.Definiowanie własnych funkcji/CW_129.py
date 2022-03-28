# %%
def filter_ge_6(words):
    filtered = []
    for word in words:
        if len(word) >= 6:
            filtered.append(word)
    return filtered


print(filter_ge_6(['Java', 'Python', 'r', 'SQL']))

# %%
