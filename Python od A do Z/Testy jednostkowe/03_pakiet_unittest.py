"""
    Tworzenie testu jednostkowego
    1. zaimportowanie unittestu
    2. zdefiniowanie funkcji do testowania
    3. stworzenie przypaddku testowego używając klasy unittest.TestCase
    4. zdefiniowanie testu jako metody klasy TestCase
    5. call assert function
    6. assert function wywoła błąd assertionError jeżeli otrzymamy błąd
    7. wywolaj funkcje main() z modułu unittest
    """
# %%
import unittest


def add(x, y):
    return x+y


class SimpleTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7, msg='Powinno być 7')


if __name__ == '__main__':
    unittest.main()

# %%
