import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(square("hello"), "bonjour") # test when 2 is given as input the output is 4.
        self.assertEqual(square("yes"), "oui")  # test when 3.0 is given as input the output is 9.0.
        self.assertNotEqual(square("amazing"), "amazing")  # test when -3 is given as input the output is not -9.


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(double("bonjour"), "hello") # test when 2 is given as input the output is 4.
        self.assertEqual(double("oui"), "yes") # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(double("étonnante"), "étonnante") # test when 0 is given as input the output is 0.

unittest.main()
