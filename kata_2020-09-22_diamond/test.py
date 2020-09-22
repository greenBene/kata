import unittest
from diamond import diamond

class TestDiamond(unittest.TestCase):
    def test(self):
        self.assertEqual(diamond('C'),'  A  \n' +
                                      ' B B \n' +
                                      'C   C\n' +
                                      ' B B \n' +
                                      '  A  ')
        self.assertEqual(diamond('A'), 'A')
        self.assertEqual(diamond('D'), '   A   \n' +
                                      '  B B  \n' +
                                      ' C   C \n' +
                                      'D     D\n' +
                                      ' C   C \n' +
                                      '  B B  \n' +
                                      '   A   ')

        self.assertRaises(Exception, diamond, '1')
        self.assertRaises(Exception, diamond, 'a')
        self.assertRaises(Exception, diamond, 'AA')

if __name__ == '__main__':
    unittest.main()
