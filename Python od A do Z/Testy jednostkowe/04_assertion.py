"""
    assertEqual - sprawdza czy dwa elemnty są  równe
    assertNotEqual - sprawddza czy ddwa elementy nie są równe
    assertTrue - sprawddza czy wyrażenie/element jest prawdą
    assertFalse - sprawddza czy wyrażenie/element jest fałszem
    assertIn - sprawdza przynależność (czy należy)
    assertNotIn - sprawdza przynależność (czy nie należy)
    """
import unittest


class SimpleTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3 + 7, 10)

    def test_sub(self):
        self.assertNotEqual(8-3, 6)

    def test_true(self):
        self.assertTrue(3+7 == 10)

    def test_false(self):
        self.assertFalse(3+7 == 11)

    def test_in(self):
        self.assertIn(3, [1, 2, 3])

    def test_not_in(self):
        self.assertNotIn(20, range(15))


if __name__ == '__main__':
    unittest.main()
