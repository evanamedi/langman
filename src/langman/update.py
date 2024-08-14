from pathlib import Path
import subprocess
import os

def update():
    """
    Pull the latest updates from the repository and reinstall the package.
    """
    try:
        # Determine the installation directory
        install_dir = Path.home() / ".langman"

        # Path to the virtual environment's Python executable
        venv_python = install_dir / "venv/bin/python"

        if not venv_python.exists():
            print("Virtual environment not found. Please set up the venv.")
            return

        # Run the git pull command to get the latest updates
        os.chdir(install_dir)
        result = subprocess.run(["git", "pull"], check=True, text=True, capture_output=True)
        
        # Check if updates were actually pulled
        if "Already up to date." not in result.stdout:
            print("Updates were pulled successfully!")
            print(result.stdout)

            # Automatically reinstall the package using the venv's Python
            print("Reinstalling the package to apply updates...")
            subprocess.run([venv_python, "-m", "pip", "install", "-e", "."], check=True)
            print("Package reinstalled successfully.")
        else:
            print("Already up to date. No changes were made.")

        print("Langman Updated Successfully\n\n")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")