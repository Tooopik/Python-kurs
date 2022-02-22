# %%
class Człowiek:

    pochodzenie = 'Ziemia'
    imie = 'Jack'


class Polak:

    kraj = 'Polska'
    imie = 'Piotr'


class Pilkarz(Człowiek, Polak):

    def info(self):
        print(
            f'Utworzony obiekt pochodzi z planety {self.pochodzenie} kraj pochodzenia: {self.kraj} Nazwa obiektu: {self.imie}')


# %%
pilkarz_1 = Pilkarz()

# %%
pilkarz_1.info()
# %%
