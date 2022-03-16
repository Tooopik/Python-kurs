# %%
numbers = ''
for i in range(10, 100):
    if i % 11 == 0:
        if len(numbers) > 0:
            numbers += ','+str(i)
        else:
            numbers += str(i)

print(numbers)

# -----------------------------------------------------------
result = []
for i in range(10, 100):
    if i % 11 == 0:
        result.append(str(i))
print(','.join(result))

# %%
