# %%
for i in '0123456789':
    i = int(i)
    if i == 6:
        print(i, type(i))
        break

# %%
sample = 'Python Course'

for char in sample:
    if char == ' ':
        break
    print(char)

# %%
for char in 'kowalskijan@gamil.com':
    if char == '@':
        print('Adres zweryfikowany')
else:
    print('Adres niezweryfikowany')
# %%
