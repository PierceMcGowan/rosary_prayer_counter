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

python3 scripts/compile_rosary.py

wine python scripts/compile_rosary.py