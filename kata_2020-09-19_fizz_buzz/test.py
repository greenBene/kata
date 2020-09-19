from fizzbuzz import fizzbuzz, fizzbuzz_advanced
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test(self):

        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(4), "4")
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(6), "Fizz")
        self.assertEqual(fizzbuzz(7), "7")
        self.assertEqual(fizzbuzz(8), "8")
        self.assertEqual(fizzbuzz(9), "Fizz")
        self.assertEqual(fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz(11), "11")
        self.assertEqual(fizzbuzz(12), "Fizz")
        self.assertEqual(fizzbuzz(13), "13")
        self.assertEqual(fizzbuzz(14), "14")
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

class TestFizzBuzzAdvanced(unittest.TestCase):
    def test(self):

        self.assertEqual(fizzbuzz_advanced(1), "1")
        self.assertEqual(fizzbuzz_advanced(2), "2")
        self.assertEqual(fizzbuzz_advanced(3), "Fizz")
        self.assertEqual(fizzbuzz_advanced(4), "4")
        self.assertEqual(fizzbuzz_advanced(5), "Buzz")
        self.assertEqual(fizzbuzz_advanced(6), "Fizz")
        self.assertEqual(fizzbuzz_advanced(7), "7")
        self.assertEqual(fizzbuzz_advanced(8), "8")
        self.assertEqual(fizzbuzz_advanced(9), "Fizz")
        self.assertEqual(fizzbuzz_advanced(10), "Buzz")
        self.assertEqual(fizzbuzz_advanced(11), "11")
        self.assertEqual(fizzbuzz_advanced(12), "Fizz")
        self.assertEqual(fizzbuzz_advanced(13), "Fizz")
        self.assertEqual(fizzbuzz_advanced(14), "14")
        self.assertEqual(fizzbuzz_advanced(15), "FizzBuzz")
        self.assertEqual(fizzbuzz_advanced(30), "FizzBuzz")
        self.assertEqual(fizzbuzz_advanced(31), "Fizz")
        self.assertEqual(fizzbuzz_advanced(51), "FizzBuzz")
        self.assertEqual(fizzbuzz_advanced(52), "Buzz")
        self.assertEqual(fizzbuzz_advanced(53), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()
