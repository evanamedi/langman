import unittest
from src.langman.language import Language

class TestLanguage(unittest.TestCase):
    def test_language_creation(self):
        language = Language(name="Python")
        self.assertEqual(language.name, "Python")
        self.assertEqual(language.keywords, [])
        self.assertEqual(language.standard_library, [])

    def test_add_keyword(self):
        language = Language(name="Python")
        language.add_keyword("def")
        self.assertIn("def", language.keywords)

    def test_add_library(self):
        language = Language(name="Python")
        language.add_library("os")
        self.assertIn("os", language.standard_library)

    def test_language_to_dict(self):
        language = Language(name="Python", keywords=["def"], standard_library=["os"])
        language_dict = language.to_dict()
        expected_dict = {
            "name": "Python",
            "keywords": ["def"],
            "standard_library": ["os"]
        }
        self.assertEqual(language_dict, expected_dict)

    def test_language_from_dict(self):
        language_data = {
            "name": "Python",
            "keywords": ["def"],
            "standard_library": ["os"]
        }
        language = Language.from_dict(language_data)
        self.assertEqual(language.name, "Python")
        self.assertIn("def", language.keywords)
        self.assertIn("os", language.standard_library)

if __name__ == "__main__":
    unittest.main()