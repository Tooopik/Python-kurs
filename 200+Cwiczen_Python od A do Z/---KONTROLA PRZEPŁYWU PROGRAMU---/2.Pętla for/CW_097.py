# %%
names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']

[print(f'Hello {name}!') for name in names if name.isalpha()]

# --------------------------------------------------------------------

for name in names:
    if name.isalpha():
        print(f'Hello {name}!')
