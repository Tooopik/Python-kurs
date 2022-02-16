# %%
from ast import Pass


class A:

    def metoda(self):
        print('Metoda klasy A')


class B(A):
    pass
   # def metoda(self):
    #    print('Metoda klasy B')


class C(A):
    pass
    # def metoda(self):
    #   print('Metoda klasy C')


class D(B, C):
    pass

   # def metoda(self):
    #    print('Metoda klasy D')


# %%
d = D()
d.metoda()

# %%
