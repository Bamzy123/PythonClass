import unittest

from corn.arrange_uppercase import arrange_uppercase_first

class TestArrangeUpperCase(unittest.TestCase):
    def test_arrange_uppercase_first_sEmIColOn(self):
        self.assertEqual(arrange_uppercase_first("sEmIColOn"), "EICOsmoln")

    def test_arrange_uppercase_first_PyThOn(self):
        self.assertEqual(arrange_uppercase_first("PyThOn"), "PTOyhn")

    def test_arrange_uppercase_first_HeLLo(self):
        self.assertEqual(arrange_uppercase_first("HeLLo"), "HLLeo")

    def test_arrange_uppercase_first_Python_WORLD(self):
        self.assertEqual(arrange_uppercase_first("WORLD"), "WORLD")

    def test_arrange_uppercase_first_lowercase(self):
        self.assertEqual(arrange_uppercase_first("lowercase"), "lowercase")

if __name__ == '__main__':
    unittest.main()