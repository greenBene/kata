import unittest
from roman import decimalToRoman

class TestRomanNumerals(unittest.TestCase):
    def test(self):
        self.assertEqual(decimalToRoman(1), 'I')
        self.assertEqual(decimalToRoman(2), 'II')
        self.assertEqual(decimalToRoman(3), 'III')
        self.assertEqual(decimalToRoman(4), 'IV')
        self.assertEqual(decimalToRoman(5), 'V')
        self.assertEqual(decimalToRoman(8), 'VIII')
        self.assertEqual(decimalToRoman(9), 'IX')
        self.assertEqual(decimalToRoman(10), 'X')
        self.assertEqual(decimalToRoman(14), 'XIV')
        self.assertEqual(decimalToRoman(36), 'XXXVI')
        self.assertEqual(decimalToRoman(49), 'XLIX')
        self.assertEqual(decimalToRoman(2020), 'MMXX')
        self.assertEqual(decimalToRoman(3999), 'MMMCMXCIX')

if __name__ == '__main__':
    unittest.main()
