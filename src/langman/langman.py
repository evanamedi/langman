#!/usr/bin/env python3
import subprocess
import os
from pathlib import Path
from .manager import Manager
from .data_handler import DataHandler
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: langman <command> [optionssss]")
        return

    command = sys.argv[1]

    if command == "remove":
        print("Remove command not yet implemented.")
        return

    if command == "add":
        print("Add command not yet implemented.")
        return

    if command == "list":
        print("List command not yet implemented.")
        return
    
    if command == "update":
        update()
        return

    print(f"Unknown command: {command}")
    
def update():
    """
    pull latest update from repository
    """
    try:
        install_dir = Path(__file__).resolve().parent.parent
        os.chdir(install_dir)
        
        
        subprocess.run(["git", "pull"], check=True)
        print("Langman has been updated!")
        print("Langman Updated. Restart your terminal to apply changes")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()