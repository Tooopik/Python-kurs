# %%
i = 0
while i < 5:
    print(i)
    i += 1

# %%
n = 0
while True:
    print(n)
    if n >= 10:
        break
    else:
        n += 1

# %%
while True:
    name = input('Podaj swoje imie: ')
    if len(name) >= 3 and name.isalpha():
        break
print('Cześć {}'. format(name))

# %%
n = 0

while n < 200:
    n += 1
    if n % 2 != 0:
        continue
    print(n)

# %%
lista_do_przeszukania = [12, 53, 13, 34]
flaga = False
wartość = 63

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartość:
        flaga = True
        break
    idx += 1
if flaga == True:
    print('Zanaleziono element {} na pozycji {}'. format(wartość, idx))
else:
    print('Nie znaleziono elemtu {}'.format(wartość))
    wybor = input('Czy dodać elemnt "{}" do listy? (t/n): '.format(wartość))
    if wybor == 't':
        lista_do_przeszukania.append(wartość)
        print(lista_do_przeszukania)


# %%
