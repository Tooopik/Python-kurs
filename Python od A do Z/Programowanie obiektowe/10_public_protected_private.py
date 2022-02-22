# public: zmienna
# protected: _zmienna
# private: __zmienna

# %%

class Spolka:
    def __init__(self, rodzaj, rynek, gielda):
        self.rodzaj = rodzaj
        self._rynek = rynek
        self.__gielda = gielda


class KGHM(Spolka):

    def __init__(self, rodzaj, rynek, gielda, nazwa):
        super().__init__(rodzaj, rynek, gielda)
        self.nazwa = nazwa
        print(f'Atrybut publiczny: {self.rodzaj}')
        print(f'Atrybut chroniony: {self._rynek}')
        #print(f'Atrybut prywatny: {self.__gielda}')


# %%
spolka_1 = Spolka('Spółka akcyjna', 'Główny', 'GPW w Warszawie')
print(f'Atrybut publiczny: {spolka_1.rodzaj}')
print(f'Atrybut chroniony: {spolka_1._rynek}')
#print(f'Atrybut prywatny: {spolka_1.__gielda}')

# %%
kghm = KGHM('Spółka akcyjna', 'Główny', 'GPW w Warszawie', 'KGHM')

# Na siłe
print(f'Atrybut prywatny: {kghm._Spolka__gielda}')
# %%
