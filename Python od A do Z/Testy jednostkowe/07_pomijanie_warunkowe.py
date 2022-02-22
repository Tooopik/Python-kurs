"""
    Opis metod:

    unittest.skip(reason) - pomija oznaczony test

    unittest.skipIf(condition,reason) - pomija oznaczony test jeśli warunek jest prawddziwy

    unittest.skipUnless(condition,reason) - pomija oznaczony test, chyba ze warunek jest prawdziwy

    unittest.expectedFilarue() - oznacza test jako oczekiwany błąd, jeśli test będzie niepowozeniem nie zostanie policzony jako błąd

"""
import unittest


class SimpleTest(unittest.TestCase):

    x = 6
    y = 2

    @unittest.skip('Pomiń')
    def test_add(self):
        wynik = self.x + self.y
        self.assertEqual(wynik, 8)

    @unittest.skipIf(x < y, 'Pomiń')
    def test_sub(self):
        wynik = self.x - self.y
        self.assertEqual(wynik, 4)

    @unittest.skipUnless(y == 0, 'Pomiń')
    def test_div(self):
        wynik = self.x / self.y
        self.assertEqual(wynik, 3.0)

    @unittest.expectedFailure
    def test_mul(self):
        wynik = self.x * self.y
        self.assertEqual(wynik, 12)


if __name__ == '__main__':
    unittest.main()
