# %%
try:
    with open('file.txt', 'r') as file:
        content = file.read()
except:
    print('Nie znaleziono pliku.')

# %%
