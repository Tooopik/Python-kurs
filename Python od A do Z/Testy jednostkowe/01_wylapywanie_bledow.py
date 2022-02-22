# %%
from tkinter import Y

from numpy import divide


1 / 0
# %%
4 + '4'
# %%
int('f')
# %%
float('sd')

# %%
try:
    1/0

except:
    print('Nie dziel przez zero!')
# %%
try:
    1/0
except ZeroDivisionError:
    print('Nie ddziel przez zero!')

except TypeError:
    print('Zły typ')
# %%
try:
    4 + '4'
except TypeError:
    print(' Nie dodawaj tekstu do liczby')

# %%
try:
    int('m')
except ValueError:
    print('Zły tekst')
# %%
while True:
    try:
        x = int(input('Podaj liczbe: >>>'))
        break
    except ValueError:
        print('Nie wprowadziłeś poprawnej wartości')
# %%
try:
    with open('test.txt', 'r') as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print('Nie ma takiego pliku')


# %%
#raise TypeError('Błąd.')

# %%


def divide(x, y):
    try:
        x = int(x)
        y = int(y)
        return x/y
    except ZeroDivisionError:
        return 'Dzielenie przez zero!'
    except ValueError:
        return 'Niepoprawny typ danych'


print(divide(3, 0))
print(divide('1', '2'))
print(divide('1', 'd'))

# %%
