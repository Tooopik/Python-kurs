# %%
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
items_uniq = sorted(list(set(items)))
result = {}

for i in items_uniq:
    if i == 'x':
        result['x'] = 0
    elif i == 'y':
        result['y'] = 0
    else:
        result['z'] = 0

for i in items:
    if i == 'x':
        result['x'] += 1
    elif i == 'y':
        result['y'] += 1
    else:
        result['z'] += 1

print(result)

# -----------------------------------------------------------------------
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']

freq = {}
for item in items:
    if item not in freq.keys():
        freq[item] = 1
    else:
        freq[item] += 1

print(freq)
