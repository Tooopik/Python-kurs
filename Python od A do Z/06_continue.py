# %%
from zmq import has


for i in range(10):
    if i == 6:
        continue
    print(i)

# %%
for i in range(20):
    if i % 2 == 0:
        continue
    print(i)

# %%
hashtags = '#summer#holidday#free'
result = ''
for char in hashtags:
    if char == '#':
        print(result)
        result = ''
        continue
    result += char
print(result)

# %%
