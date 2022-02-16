# %%


class Drzewo:

    def __init__(self, nazwa, wiek, wysokosc):
        self.nazwa = nazwa
        self.wiek = wiek
        self.wysokosc = wysokosc

    def czy_chronione(self):
        if self.wiek >= 20 and self.wysokosc >= 20:
            print(f'Drzewo o nazwie {self.nazwa} jest pod ochroną')
        else:
            print(f'Drzewo o nazwie {self.nazwa} nie jest pod ochroną')

    def postarz_o_rok(self):
        self.wiek += 1


# %%
drzewo_1 = Drzewo('Sosna', 35, 25)

# %%
dir(drzewo_1)
# %%
drzewo_2 = Drzewo('Brzoza', 15, 18)
# %%
drzewo_2.czy_chronione()

# %%
drzewo_1.czy_chronione()

# %%
drzewo_2.postarz_o_rok()

# %%
drzewo_2.wiek

# %%
