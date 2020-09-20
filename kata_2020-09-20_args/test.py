import unittest
from args import arguments_parsing, InvalidParameterException

class TestArgumentParsing(unittest.TestCase):
    def test(self):

        self.assertEqual(arguments_parsing([]),[('-b', False), ('-s', ''), ('-i', 0), ('-l', [])])

        self.assertEqual(arguments_parsing("-b".split(' ')),[('-b', True), ('-s', ''), ('-i', 0), ('-l', [])])

        self.assertEqual(arguments_parsing("-s Benedikt".split(' ')),[('-b', False), ('-s', 'Benedikt'), ('-i', 0), ('-l', [])])

        self.assertEqual(arguments_parsing('-i 42'.split(' ')),[('-b', False), ('-s', ''), ('-i', 42), ('-l', [])])
        self.assertEqual(arguments_parsing('-i -42'.split(' ')),[('-b', False), ('-s', ''), ('-i', -42), ('-l', [])])

        self.assertEqual(arguments_parsing('-l hello,world,what\'s,up'.split(' ')),[('-b', False), ('-s', ''), ('-i', 0), ('-l', ['hello', 'world', 'what\'s', 'up'])])

        self.assertEqual(arguments_parsing('-i 42 -b -l hello,world -s Benedikt'.split(' ')),[('-b', True), ('-s', 'Benedikt'), ('-i', 42), ('-l', ['hello', 'world'])])

        self.assertRaises(InvalidParameterException, arguments_parsing, '-i asdfasdf'.split(' '))
        self.assertRaises(InvalidParameterException, arguments_parsing, '-i'.split(' '))
        self.assertRaises(InvalidParameterException, arguments_parsing, '-i --8'.split(' '))
        self.assertRaises(InvalidParameterException, arguments_parsing, '-s'.split(' '))
        self.assertRaises(InvalidParameterException, arguments_parsing, '-l'.split(' '))


if __name__ == '__main__':
    unittest.main()
