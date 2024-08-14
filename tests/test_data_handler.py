import unittest
import json
from pathlib import Path
from src.langman.data_handler import DataHandler
from src.langman.language import Language
from src.langman.program import Program

class TestDataHandler(unittest.TestCase):
    def setUp(self):
        self.root_path = Path(__file__).parent.parent
        self.test_file = self.root_path / "test_data.json"
        self.data_handler = DataHandler(str(self.test_file))

    def tearDown(self):
        if self.test_file.exists():
            self.test_file.unlink()

    def test_save_and_load_language(self):
        language = Language(name="Python", keywords=["def"], standard_library=["os"])
        data = {"Python": language}

        self.data_handler.save_data(data)

        loaded_data = self.data_handler.load_data()
        loaded_language = loaded_data.get("Python")

        self.assertIsNotNone(loaded_language)
        self.assertEqual(loaded_language.name, "Python")
        self.assertIn("def", loaded_language.keywords)
        self.assertIn("os", loaded_language.standard_library)

    def test_save_and_load_program(self):
        program = Program(name="MyProgram", version="2.0")
        data = {"MyProgram": program}

        self.data_handler.save_data(data)

        loaded_data = self.data_handler.load_data()
        loaded_program = loaded_data.get("MyProgram")

        self.assertIsNotNone(loaded_program)
        self.assertEqual(loaded_program.name, "MyProgram")
        self.assertEqual(loaded_program.version, "2.0")

    def test_load_empty_data(self):
        self.test_file.write_text(json.dumps({}))

        loaded_data = self.data_handler.load_data()
        self.assertEqual(loaded_data, {})

if __name__ == "__main__":
    unittest.main()