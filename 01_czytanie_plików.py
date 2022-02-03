# %%
file = open('simple.txt', 'r')

for linie in file:
    print(linie, end='')

file.close()

# %%
with open('simple.txt', 'r') as file:
    for line in file:
        print(line, end='')

# %%
'''Najczęściej stosowane tryby otwierania plików:

'r' - read - otwiera plik do odczytu, zwraca błąd jeśli plik nie istnieje

'a' - append - otwiera plik do dopisania, tworzy plik jeśli nie istnieje

'w' - write - otwiera plik do zapisu, tworzy plik jeśli nie istnieje
'''
# %%
with open('simple.txt', 'r') as file:
    line = file.readline()
    print(line)

# %%
with open('simple.txt', 'r') as file:
    line = file.readlines()
    print(line)

# %%
with open('simple.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')

# %%
with open('simple.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()

# %%
with open('simple.txt', 'r') as file:
    lines = file.read()
    print(lines)
