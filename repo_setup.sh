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

# Ensure required tools are installed
echo "Installing dependencies..."
pip install black mypy pylint

# Run black
echo "Running black..."
black python_lib/divine_mercy python_lib/rosary python_lib/counter_gui

# Run mypy
echo "Running mypy..."
mypy python_lib/divine_mercy python_lib/rosary python_lib/counter_gui

# Run pylint
echo "Running pylint..."
pylint python_lib/divine_mercy python_lib/rosary python_lib/counter_gui

echo "All checks completed!"

pip install --editable ./python_lib/counter_gui
pip install --editable ./python_lib/divine_mercy
pip install --editable ./python_lib/rosary