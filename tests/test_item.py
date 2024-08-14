import unittest
from src.langman.item import Item

class TestItem(unittest.TestCase):
    def test_item_creation(self):
        item = Item(name="TestItem")
        self.assertEqual(item.name, "TestItem")
    
    def test_item_to_dict(self):
        item = Item(name="TestItem")
        item_dict = item.to_dict()
        expected_dict = {"name": "TestItem"}
        self.assertEqual(item_dict, expected_dict)
    
    def test_item_from_dict(self):
        item_data = {"name": "TestItem"}
        item = Item.from_dict(item_data)
        self.assertEqual(item.name, "TestItem")

if __name__ == "__main__":
    unittest.main()