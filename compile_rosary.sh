# Set up a Python virtual environment
VENV_DIR=".venv"

if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment already exists. Activating..."
else
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Ensure required tools are installed
echo "Installing dependencies..."
pip install --upgrade pip
pip uninstall -y rosary divine_mercy counter_gui
pip cache purge
pip install -r requirements.txt

pip install ./python_lib/counter_gui
pip install ./python_lib/divine_mercy
pip install ./python_lib/rosary

# Compile for Linux
python3 scripts/compile_rosary.py

# Install Python packages into Wine's Windows Python and set up a virtual environment
if command -v wine >/dev/null 2>&1 && [ -f "$HOME/.wine/drive_c/Python311/python.exe" ]; then
    echo "Setting up Wine Python instance and virtual environment..."
    wine $HOME/.wine/drive_c/Python311/python.exe -m pip install --upgrade pip
    wine $HOME/.wine/drive_c/Python311/python.exe -m pip install virtualenv
    # Create a virtual environment in Wine's C: drive if it doesn't exist
    if [ ! -d "$HOME/.wine/drive_c/pyenv" ]; then
        wine $HOME/.wine/drive_c/Python311/python.exe -m virtualenv C:\\pyenv
    fi
    # Activate the Wine virtual environment and install dependencies
    wine $HOME/.wine/drive_c/pyenv/Scripts/pip.exe install -r requirements.txt
    wine $HOME/.wine/drive_c/pyenv/Scripts/pip.exe install --editable ./python_lib/counter_gui
    wine $HOME/.wine/drive_c/pyenv/Scripts/pip.exe install --editable ./python_lib/divine_mercy
    wine $HOME/.wine/drive_c/pyenv/Scripts/pip.exe install --editable ./python_lib/rosary

    wine $HOME/.wine/drive_c/pyenv/Scripts/python.exe scripts/compile_rosary.py
else
    echo "Wine or Windows Python not found. Skipping Wine Python setup."
fi