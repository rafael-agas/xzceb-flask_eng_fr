import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Good morning"), "Bonjour")
        self.assertEqual(english_to_french("Good evening"), "Bonsoir ")
        self.assertNotEqual(english_to_french("Goodbye"), "Adios")
        self.assertNotEqual(english_to_french("How are you"), "How are you")

class TestFrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Bonne soirée"), "Good evening")
        self.assertNotEqual(french_to_english("deux"), "three")
        self.assertNotEqual(french_to_english("trois"), "trois")

unittest.main()