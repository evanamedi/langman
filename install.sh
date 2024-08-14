#!/bin/bash

# installation directory
INSTALL_DIR="$HOME/.langman"
VENV_DIR="$INSTALL_DIR/venv"
BIN_DIR="$HOME/bin"
WRAPPER_SCRIPT="$BIN_DIR/langman"

# make sure ~/bin directory exists
mkdir -p "$BIN_DIR"

# create isntallation directory if it doesn't exist
mkdir -p "$INSTALL_DIR"

# set up Python venv
python3.12 -m venv "$VENV_DIR"

# activate venv
source "$VENV_DIR/bin/activate"

# install packages in venv
pip install .

# write wrapper script in ~/bin to run command within venv
cat <<EOL > "$WRAPPER_SCRIPT"
#!/bin/bash
source "$VENV_DIR/bin/activate"
exec langman "\$@"
EOL

# make wrapper script executable
chmod +x "$WRAPPER_SCRIPT"

# ensure ~/bin is in the users PATH
if ! echo"$PATH" | grep -q "$HOME/bin"; then
	echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.bashrc"
	echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.zshrc"
	echo "Added $HOME/bin to Path in .bashrc and .zshrc"
fi

echo "Installation compelete. Restart temrinal to start using langman"