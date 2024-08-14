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
    Pull the latest updates from the repository and apply changes.
    """
    try:
        # Determine the installation directory
        install_dir = Path(__file__).resolve().parent.parent
        os.chdir(install_dir)

        # Ensure the virtual environment is activated
        venv_activate = install_dir / "venv/bin/activate"
        if not venv_activate.exists():
            print("Virtual environment not found. Please set up the venv.")
            return

        # Run the git pull command
        result = subprocess.run(["git", "pull"], check=True, text=True, capture_output=True)
        if "Already up to date." not in result.stdout:
            print("Updates were pulled successfully!")
            print(result.stdout)

            # Reinstall the package if there were updates
            print("Reinstalling the package to apply updates...")
            subprocess.run([str(install_dir / "venv/bin/pip"), "install", "-e", "."], check=True)
            print("Package reinstalled successfully.")
        else:
            print("Already up to date.")

        print("Langman Updated. Restart your terminal to apply changes.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()