# %%
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
toRemove = []

for i in items:
    if i % 2 != 0:
        toRemove.append(i)

for i in toRemove:
    items.remove(i)

print(items)

# ----------------------------------------------------------
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
result = []
for item in items:
    if not item % 2 != 0:
        result.append(item)
print(result)
