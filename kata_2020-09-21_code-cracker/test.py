import unittest
from code_cracker import decrypt

class TestCodeCracker(unittest.TestCase):
    def test(self):
        self.assertEqual(decrypt('! ) " ( £ * % & > < @ a b c d e f g h i j k l m n o'),
                                 'a b c d e f g h i j k l m n o p q r s t u v w x y z')
        self.assertEqual(decrypt(')£c£(>@i'), 'benedikt')
        self.assertEqual(decrypt('i&>h >h ldg@>c%'), 'this is working')

if __name__ == '__main__':
    unittest.main()
