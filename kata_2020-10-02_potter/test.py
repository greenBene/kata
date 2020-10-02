import unittest
from potter import price

class TestBasic(unittest.TestCase):
    def test(self):
        self.assertEqual(0, price([]))
        self.assertEqual(8, price([0]))
        self.assertEqual(8, price([1]))
        self.assertEqual(8, price([2]))
        self.assertEqual(8, price([3]))
        self.assertEqual(8, price([4]))
        self.assertEqual(3 * 8, price([1,1,1,]))

class TestSimpleDiscounts(unittest.TestCase):
    def test(self):
        self.assertEqual(0.95 * 2 * 8, price([0,1]))
        self.assertEqual(0.90 * 3 * 8, price([0,1,2]))
        self.assertEqual(0.80 * 4 * 8, price([0,1,2,3]))
        self.assertEqual(0.75 * 5 * 8, price([0,1,2,3,4]))

class TestMultipleDiscounts(unittest.TestCase):
    def test(self):
        self.assertEqual(8 + 0.95 * 2 * 8, price([0,1,1]))
        self.assertEqual(0.95 * 2 * 8 + 0.95 * 2 * 8, price([0,0,1,1]))
        self.assertEqual(0.8 * 4 * 8 + 0.9 * 3 * 8, price([0,0,1,1,2,2,3]))
        self.assertEqual(0.75 * 5 * 8 + 8, price([0,0,1,2,3,4]))

class TestMultipleDiscountsEdgeCases(unittest.TestCase):
    def test(self):
        self.assertEqual(0.8 * 4 * 8 + 0.8 * 4 * 8, price([0,0,1,1,2,2,3,4]))


if __name__ == '__main__':
    unittest.main()
