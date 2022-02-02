# %%
fakt = 'python jest łatwy i przyjemny'
characters = list(fakt)
lenght = len(set(characters))

if lenght < 20:
    print('Mniej niż 20 unikalnych znaków.')

else:
    print('Liczba unikalnych znaków jest większa lub równa 20')
# %%
if len(set(fakt)) < 20:
    print('Mniej niż 20 unikalnych znaków.')

else:
    print('Liczba unikalnych znaków jest większa lub równa 20')
