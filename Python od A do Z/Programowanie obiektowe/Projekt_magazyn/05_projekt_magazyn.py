# %%
import sys


class Magazyn:

    def __init__(self, lista_produktow):
        self.lista_produktow = lista_produktow

    def wyswietl_dostepne_produkty(self):
        print('Dostępne produkty: ')
        for produkt in self.lista_produktow:
            print(produkt)

    def dodaj_produkt(self):
        self.nazwa_produktu = input('Podaj nazwe produktu: >>> ')
        if self.nazwa_produktu not in self.lista_produktow:
            self.lista_produktow.append(self.nazwa_produktu)
            print(f'Produkt {self.nazwa_produktu} został dodany do magazynu')

    def usun_produkt(self):
        self.nazwa_produktu = input(
            'Podaj nazwe produktu, który chcesz usunąć: >>> ')
        if self.nazwa_produktu in self.lista_produktow:
            self.lista_produktow.remove(self.nazwa_produktu)
            print(f'Produkt {self.nazwa_produktu} usunięto z magazynu')

        else:
            print(f'Produkt {self.nazwa_produktu} nie istnieje w magazynie.')


# %%
magazyn = Magazyn(['mleko', 'woda', 'jajka'])

while True:
    print("="*50)
    print('Wprowadź 1 aby wyświetlić stan magazynu.')
    print('Wprowadź 2 aby dodać produkt.')
    print('Wprowadź 3 aby usunąć produkt.')
    print('Wprowadź 4 aby zakończyć.')
    print("="*50)
    wybor_urzytkownika = int(input('>>> '))
    if wybor_urzytkownika is 1:
        magazyn.wyswietl_dostepne_produkty()
    elif wybor_urzytkownika is 2:
        magazyn.dodaj_produkt()
    elif wybor_urzytkownika is 3:
        magazyn.usun_produkt()
    elif wybor_urzytkownika is 4:
        sys.exit()

# %%
