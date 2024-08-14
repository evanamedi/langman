#!/bin/bash

# Define the installation directory
INSTALL_DIR="$HOME/.langman"
VENV_DIR="$INSTALL_DIR/venv"
BIN_DIR="$HOME/bin"
WRAPPER_SCRIPT="$BIN_DIR/langman"

# Ensure ~/bin directory exists
mkdir -p "$BIN_DIR"

# Create the installation directory if it doesn't exist
mkdir -p "$INSTALL_DIR"

# Clone the repo or download the necessary files (if not already done)
cd "$INSTALL_DIR"
if [ ! -d "$INSTALL_DIR/langman" ]; then
    git clone https://github.com/evanamedi/langman.git .
fi

# Set up a Python virtual environment in the installation directory
python3 -m venv "$VENV_DIR"

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Navigate to the directory containing setup.py
cd "$INSTALL_DIR"

# Check if setup.py exists before attempting to install
if [ ! -f setup.py ]; then
    echo "Error: setup.py not found in the current directory."
    exit 1
fi

# Install the package in the virtual environment
pip install .

# Write the wrapper script in ~/bin to run the command within the venv
cat <<EOL > "$WRAPPER_SCRIPT"
#!/bin/bash
source "$VENV_DIR/bin/activate"
exec langman "\$@"
EOL

# Make the wrapper script executable
chmod +x "$WRAPPER_SCRIPT"

# Ensure ~/bin is in the user's PATH
if ! echo "$PATH" | grep -q "$HOME/bin"; then
    echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.bashrc"
    echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.zshrc"
    echo "Added $HOME/bin to PATH in .bashrc and .zshrc"
fi

echo "Installation complete! Please restart your terminal or run 'source ~/.bashrc' to start using langman."