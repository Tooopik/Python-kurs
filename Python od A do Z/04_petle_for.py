# %%
for i in 'python':
    print(i)

# %%
name = 'python is the beast!'
index = 0

for i in name:
    print(index, i)
    index += 1
# %%
for index in range(10):
    print(index)

# %%
name = 'Adrian'
for index in range(len(name)):
    print(index, name[index])

# %%
name = 'Adrian'
for i in enumerate(name):
    print(i)

# %%
name = 'Adrian'
for index, character in enumerate(name):
    print(index, character)

# %%
for i, value in enumerate([4, 5, 6, 8, 6]):
    print(i, value)

# %%
for i in range(10):
    print(i)

# %%
for i in range(10, 20):
    print(i)

# %%
for i in range(10, 20, 2):
    print(i)

# %%
for i in range(10, 0, -1):
    print(i)

# %%
for i in range(10, 100, 10):
    print(i)

# %%
string = 'Python Course'
for char in string:
    print(char)

# %%
string = 'Python Course'
for char in string[:6]:
    print(char)

# %%
string = 'Python Course'
for char in string[::2]:
    print(char)

# %%
string = 'Python Course'
for char in string[::-1]:
    print(char)

# %%
hashtags = '#sport#gym#fitness'

for char in hashtags:
    print(char)

# %%
hashtags = '#sport#gym#fitness'

for char in hashtags:
    if char not in "#":
        print(char)

# %%
for char in zip('abcde', '12345'):
    print(char)

# %%
for char, number in zip('abc', '12345'):
    print(char, number)

# %%
result = ''

for char in hashtags:
    if char not in '#':
        result += char
    else:
        print(result)
        result = ''
print(result)
result = ''

# %%
