# %%
def parabola(x):
    return x**2+3


print(type(parabola))
print(parabola(30))

# %%
funkcja_1 = parabola

print(funkcja_1(30))

# %%
lambda x: x**2 + 3
# %%
def f(x): return x**2 + 3


f(30)

# %%


def f_2(word): return word.upper()


f_2('python')

# %%


def add(x, y): return x+y


add(3, 5)

# %%


def f_4(word_1, word_2): return word_1 + ' ' + word_2


f_4('hello', 'world')

# %%
lista = ['python', 'java', 'r', 'sql']
list(map(lambda word: word.upper(), lista))

# %%


def make_upper(word):
    return word.upper()


list(map(make_upper, lista))

# %%
list(map(lambda word: word.title(), lista))

# %%
list(map(lambda word: (word, len(word)), lista))
# %%


def apply_function(x, fn):
    return fn(x)


apply_function(5, lambda x: x**2)

# %%
apply_function([12, 45], lambda x: sum(x))

# %%
numbers = [1, 5, 6, 7, 0, 4, 6]
sorted(numbers)

# %%
numbers = [-3, -2, -1, 0, 1, 2, 3]
sorted(numbers, key=lambda x: abs(x))

# %%
lista = [('jeden', 'one'), ('dwa', 'two'), ('trzy', 'three')]

sorted(lista)
sorted(lista, key=lambda x: x[1])

# %%
