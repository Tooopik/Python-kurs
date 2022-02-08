# %%
results = []

for i in range(100):
    results.append(i**2)

print(results)

# %%
results_2 = [i**2 for i in range(100)]

# %%
lista = [i for i in range(100)]

# %%
results_3 = []

for i in range(100):
    if i % 5 == 0:
        results_3.append(i**2)

print(results)

# %%
results_4 = [i**2 for i in range(100) if i % 5 == 0]

# %%
letters = ['a', 'b', 'c']
numbers = ['1', '2', '3']

results = []
for letter in letters:
    for number in numbers:
        results.append(letter+number)

# %%
letters = ['a', 'b', 'c']
numbers = ['1', '2', '3']

results_5 = [letter+number for letter in letters for number in numbers]
# %%
letters_1 = ['a', 'b', 'c']
letters_2 = ['a', 'b', 'c']

results = [l_1 + l_2 for l_1 in letters_1 for l_2 in letters_2 if l_1 != l_2]

# %%
[[j for j in range(10)] for i in range(10)]
# %%
[[(i, j) for j in range(10)] for i in range(10)]

# %%
[[i*j for j in range(10)] for i in range(10)]

# %%
[[l1+l2 for l2 in 'abcde'] for l1 in '12345']
# %%


def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*silnia(n-1)


[silnia(i) for i in range(10)]
# %%
