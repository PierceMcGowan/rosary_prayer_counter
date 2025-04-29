#!/bin/bash

# Check if .venv directory exists
if [ ! -d ".venv" ]; then
    echo "Creating Python virtual environment in .venv..."
    python3 -m venv .venv
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
echo "Activating the virtual environment..."
source .venv/bin/activate

# Confirm activation
if [ "$VIRTUAL_ENV" != "" ]; then
    echo "Virtual environment activated: $VIRTUAL_ENV"
else
    echo "Failed to activate the virtual environment."
fi