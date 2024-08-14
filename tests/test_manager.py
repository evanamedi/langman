import unittest
import json
from unittest.mock import MagicMock
from src.langman.manager import Manager
from src.langman.language import Language
from src.langman.program import Program
from src.langman.data_handler import DataHandler
from src.langman.item import Item
from pathlib import Path


class TestManager(unittest.TestCase):
    def setUp(self):
        self.data_handler = MagicMock(spec=DataHandler)
        self.data_handler.load_data.return_value = {}
        self.manager = Manager(self.data_handler)

        self.root_path = Path(__file__).parent.parent
        self.dev_file_path = self.root_path / "dev_data.json"
        if not self.dev_file_path.exists():
            self.dev_file_path.write_text(json.dumps({
                "TestLanguage": {
                    "name": "TestLanguage",
                    "keywords": ["test"],
                    "standard_library": ["testlib"]
                }
            }))

    def tearDown(self):
        if self.dev_file_path.exists():
            self.dev_file_path.unlink()

    def merge_with_dev_data(self):
        dev_file_path = Path(__file__).parent.parent / 'dev_data.json'
        if not dev_file_path.exists():
            print(f"Dev data file not found at {dev_file_path}")
            return

        with open(dev_file_path, 'r') as dev_file:
            dev_data = json.load(dev_file)
            print(f"Loaded dev data: {dev_data}")

        # Merge dev data into user data without overwriting user customizations
        for name, item_data in dev_data.items():
            if name not in self.items:  # Only add if the item doesn't already exist
                if item_data.get("keywords") is not None:
                    self.items[name] = Language.from_dict(item_data)
                elif item_data.get("version") is not None:
                    self.items[name] = Program.from_dict(item_data)
                else:
                    self.items[name] = Item.from_dict(item_data)
        print(f"Final items after merge: {self.items}")

        # Save the updated data
        self.data_handler.save_data(self.items)

    def test_add_language(self):
        self.manager.add_item("language", "Python")
        self.assertIn("Python", self.manager.items)
        self.assertIsInstance(self.manager.items["Python"], Language)

    def test_add_program(self):
        self.manager.add_item("program", "MyProgram")
        self.assertIn("MyProgram", self.manager.items)
        self.assertIsInstance(self.manager.items["MyProgram"], Program)

    def test_remove_item(self):
        self.manager.add_item("language", "Python")
        self.manager.remove_item("Python")
        self.assertNotIn("Python", self.manager.items)

    def test_get_item(self):
        self.manager.add_item("language", "Python")
        item = self.manager.get_item("Python")
        self.assertIsNotNone(item)
        self.assertEqual(item.name, "Python")

    def test_list_items(self):
        self.manager.add_item("language", "Python")
        self.manager.add_item("program", "MyProgram")
        items = self.manager.list_items()
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0].name, "Python")
        self.assertEqual(items[1].name, "MyProgram")

    def test_data_handler_save_called(self):
        self.manager.add_item("language", "Python")
        self.data_handler.save_data.assert_called_once()

    def test_data_handler_load_called(self):
        self.data_handler.load_data.assert_called_once()

if __name__ == "__main__":
    unittest.main()