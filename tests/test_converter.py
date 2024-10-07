import unittest
from src.converter import NumberToFrenchConverter

class TestNumberToFrenchConverter(unittest.TestCase):
    
    def setUp(self):
        self.converter = NumberToFrenchConverter()

    def test_basic_numbers(self):
        self.assertEqual(self.converter.convert(0), "zéro")
        self.assertEqual(self.converter.convert(15), "quinze")
    
    def test_tens(self):
        self.assertEqual(self.converter.convert(21), "vingt-et-un")
        self.assertEqual(self.converter.convert(99), "quatre-vingt-dix-neuf")
    
    def test_hundreds(self):
        self.assertEqual(self.converter.convert(100), "cent")
        self.assertEqual(self.converter.convert(555), "cinq cent cinquante-cinq")
    
    def test_thousands(self):
        self.assertEqual(self.converter.convert(1000), "mille")
        self.assertEqual(self.converter.convert(1234), "mille deux cent trente-quatre")

    def test_large_numbers(self):
        self.assertRaises(ValueError, self.converter.convert, 1000000)

if __name__ == '__main__':
    unittest.main()
