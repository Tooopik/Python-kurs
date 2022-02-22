# %%
abs(10)
# %%
abs(-10)

# %%
print(abs(-11))

# %%
bool([])

# %%
bool('')

# %%
bool({})

# %%
bool(' ')

# %%
bool(True)

# %%
bool(1)
# %%
bool(0)

# %%
dir(list)

# %%
dir(tuple)

# %%
list(enumerate(['Paweł', 'Python', 'Java']))

# %%
eval('1 +1')

# %%
x = 10
eval('x+13')

# %%
list(filter(abs, [-2, -1, 0, 1, 2]))

# %%
list(filter(bool, ['python', '', 'java']))
# %%
float(1)

# %%
float(1.3)
# %%
float('1')
# %%
float('ffr')

# %%
float('3.5')

# %%
help()
# %%
help(float)

# %%
help(int)

# %%
isinstance(1, int)

# %%
isinstance(1, float)

# %%
isinstance('scdfr', str)

# %%
isinstance('', str)

# %%
len('python')

# %%
len('')

# %%
len(' ')

# %%
len([])

# %%
len([[3, 4], [[5, 6], [7, 8]]])

# %%
list('python')

# %%
list(range(10))

# %%
list(map(abs, [-2, -1, 0, 1, 2]))

# %%
names = ['adrian', 'anna', 'grzegorz', 'marzena']
list(map(str.title, names))

# %%
max([1, 2, 3, 4, 5, 6])

# %%
max('pawel')

# %%
max('tomek')

# %%
min([1, 2, 3, 4, 5, 6])

# %%
min('tomek')
# %%
min('pawel')

# %%
pow(2, 4)

# %%
2 ** 4

# %%
list(reversed([1, 2, 3, 4, 5, 6, 7, 8]))

# %%
list(reversed([1, 5, 3, 4, 5, 2, 7, 8]))

# %%
list(reversed('python'))

# %%
round(4.3567892)

# %%
round(4.3567892, 3)

# %%
str(1)

# %%
str(34.11)

# %%
sum([3, 6, 4, 8])

# %%
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
list(zip(lista_1, lista_2))

# %%
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6, 5]
list(zip(lista_1, lista_2))

# %%
list(zip('python', 'course'))

# %%
