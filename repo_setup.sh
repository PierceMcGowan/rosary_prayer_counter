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
pip uninstall -y rosary divine_mercy
pip cache purge
pip install -r python_code/requirements.txt

# Ensure required tools are installed
echo "Installing dependencies..."
pip install black mypy pylint

# Run black
echo "Running black..."
black prayers/divine_mercy prayers/rosary

# Run mypy
echo "Running mypy..."
mypy prayers/divine_mercy prayers/rosary

# Run pylint
echo "Running pylint..."
pylint prayers/divine_mercy prayers/rosary

echo "All checks completed!"

pip install --editable prayers/divine_mercy prayers/rosary
