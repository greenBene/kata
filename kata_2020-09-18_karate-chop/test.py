from binary_chop import chop_while
import unittest

class TestBinarychop_while(unittest.TestCase):
    def test(self):

        self.assertEqual(chop_while(3, []), -1)
        self.assertEqual(chop_while(3, [1]), -1)
        self.assertEqual(chop_while(1, [1]), 0)

        self.assertEqual(chop_while(1, [1, 3, 5]), 0)
        self.assertEqual(chop_while(3, [1, 3, 5]), 1)
        self.assertEqual(chop_while(5, [1, 3, 5]), 2)
        self.assertEqual(chop_while(0, [1, 3, 5]), -1)
        self.assertEqual(chop_while(2, [1, 3, 5]), -1)
        self.assertEqual(chop_while(4, [1, 3, 5]), -1)
        self.assertEqual(chop_while(6, [1, 3, 5]), -1)

        self.assertEqual(chop_while(1, [1, 3, 5, 7]), 0)
        self.assertEqual(chop_while(3, [1, 3, 5, 7]), 1)
        self.assertEqual(chop_while(5, [1, 3, 5, 7]), 2)
        self.assertEqual(chop_while(7, [1, 3, 5, 7]), 3)
        self.assertEqual(chop_while(0, [1, 3, 5, 7]), -1)
        self.assertEqual(chop_while(2, [1, 3, 5, 7]), -1)
        self.assertEqual(chop_while(4, [1, 3, 5, 7]), -1)
        self.assertEqual(chop_while(6, [1, 3, 5, 7]), -1)
        self.assertEqual(chop_while(8, [1, 3, 5, 7]), -1)


if __name__ == '__main__':
    unittest.main()
