import os
import subprocess
import sys
from .manager import Manager
        
def add_(manager: Manager, item_type: str, name:str):
    if item_type not in ["language", "program"]:
        print(f"Unkown item type: {item_type}")
        return
    
    manager.add_item(item_type, name)
    print(f"{item_type.capitalize()} '{name}' added")

def remove_(manager: Manager, name: str):
    if manager.get_item(name):
        manager.remove_item(name)
        print(f"Item '{name}' removed")
    else:
        print(f"Item '{name}' not found")

def list_(manager: Manager):
    items = manager.list_items()
    if not items:
        print("No items found")
    else:
        for item in items:
            print(item.name)

def open_data_file():
    file_path = 'data.json'
    if sys.platform == "win32":
        os.startfile(file_path)
    elif sys.platform == "darwin":
        subprocess.run(["open", file_path])
    else:
        subprocess.run(["xdg-open", file_path])
