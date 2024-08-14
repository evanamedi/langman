import sys
from .commands import add_, remove_, list_, open_data_file
from .update import update
from .manager import Manager
from .data_handler import DataHandler

def main():
    command_list = ["add", "remove", "list", "update", "open"]
    if len(sys.argv) < 2:
        print("Command Options:\n,")
        print(command_list)
        return

    command = sys.argv[1]
    
    data_handler = DataHandler('data.json')
    manager = Manager(data_handler)

    commands = {
        "add": lambda: add_(manager, sys.argv[2]) if len(sys.argv) > 2 else print("Provide a name to remove"),
        "remove": lambda: remove_(manager, sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else print("provide an item type and name")),
        "list": lambda: list_(manager),
        "update": update,
        "open": open_data_file
    }
    
    command_func = commands.get(command)
    if command_func:
        command_func()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()