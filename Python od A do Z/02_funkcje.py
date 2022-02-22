# %%
import math


def funkcja_1():
    print('Pierwsza funkcja uruchomiona.')


funkcja_1()

# %%


def funkcja_2(x, y):
    print('Podane argumenty to :  x = {0}, y = {1}'.format(x, y))


funkcja_2(1, 2)

# %%


def funkcja_2(x, y=10):
    print('Podane argumenty to :  x = {0}, y = {1}'.format(x, y))


funkcja_2(1)

# %%

math.sqrt(2)
math.exp(1)
math.sin(1)
# %%


def funkcja_3():
    print('uruchomiono')


funkcja_3()

# %%


def add(x, y):
    return x+y


print(add(2, 6))

# %%


def substract(x: int, y: int):
    """Odejmuje od siebie dwie liczby

    Args:
        x (int): [description]
        y (int): [description]

    Returns:
        [int]: [description]
    """
    return x-y


substract(10, 6)

# %%


def print_menu():
    print('start programu')
    print('*'*30)
    print(""" Wybierz jedna z podanych opcji:
    0 - logowanie
    1 - wyjście """)
    print('*'*30)
    print('Koniec programu')


print_menu()

# %%


def print_even(maximum):
    even = []
    for i in range(maximum+1):
        if i % 2 == 0:
            even.append(i)
    return even


print_even(10)
num = print_even(20)

# %%


def write_file(file_name, text):
    with open(file_name, 'w') as file:
        print(text, file=file)


write_file('sample.txt', 'Pierwsza linia.\nDruga linia.')
write_file('sample_2.txt', 'Pierwsza.\nDruga.\nTrzecia.')
# %%


def calculate_profit(pv=1000, rate=0.03, n=1):
    return pv*(1+rate)**n - pv


calculate_profit(1000, 0.2, 15)
calculate_profit()
calculate_profit(rate=0.4)

# %%
