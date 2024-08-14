import json
from pathlib import Path
from .item import Item
from .language import Language
from .program import Program

class DataHandler:
    def __init__(self, file_path: str = 'data.json'):
        root_path = Path(__file__).parent.parent
        self.file_path = root_path / file_path

    def load_data(self):
        if self.file_path.exists():
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                items = {}
                for name, item_data in data.items():
                    if item_data.get("keywords") is not None:
                        items[name] = Language.from_dict(item_data)
                    elif item_data.get("version") is not None:
                        items[name] = Program.from_dict(item_data)
                    else:
                        items[name] = Item.from_dict(item_data)
                return items
        return {}

    def save_data(self, data):
        with open(self.file_path, 'w') as f:
            json.dump({name: item.to_dict() for name, item in data.items()}, f, indent=4)