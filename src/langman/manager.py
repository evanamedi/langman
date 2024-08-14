from .language import Language
from .program import Program
import json
from .item import Item
from pathlib import Path
class Manager:
    def __init__(self, data_handler):
        self.data_handler = data_handler
        self.items = self.data_handler.load_data()
        self.merge_with_dev_data()
        
    def merge_with_dev_data(self):
        dev_file_path = Path(__file__).parent.parent / "dev_data.json"
        if not dev_file_path.exists():
            return
        
        with open(dev_file_path, 'r') as dev_file:
            dev_data = json.load(dev_file)
        
        for name, item_data in dev_data.items():
            if name not in self.items:
                if item_data.get("keywords") is not None:
                    self.items[name] = Language.from_dict(item_data)
                elif item_data.get("version") is not None:
                    self.items[name] = Program.from_dict(item_data)
                else:
                    self.items[name] = Item.from_dict(item_data)
        
        self.data_handler.save_data(self.items)

    def add_item(self, item_type: str, name: str) -> None:
        if item_type == "language":
            item = Language(name)  # Create a new Language instance
        elif item_type == "program":
            item = Program(name)  # Create a new Program instance
        else:
            print(f"Unknown item type: {item_type}")
            return
        
        self.items[name] = item
        self.data_handler.save_data(self.items)  # Save the updated items

    def remove_item(self, name: str) -> None:
        if name in self.items:
            del self.items[name]
            self.data_handler.save_data(self.items)  # Save the updated items

    def get_item(self, name: str):
        return self.items.get(name)

    def list_items(self) -> list:
        return list(self.items.values())