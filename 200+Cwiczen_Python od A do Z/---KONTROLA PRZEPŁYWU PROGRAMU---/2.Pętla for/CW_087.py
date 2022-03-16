# %%
numbers = []
for i in range(10, 100):
    if i % 11 == 0 and i % 3 != 0:
        numbers.append(str(i))

print(','.join(numbers))

# %%
