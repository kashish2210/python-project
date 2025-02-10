#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install required dependencies
pip install flask
pip install gunicorn uvicorn

echo "Setup complete! Virtual environment is ready with Flask, Gunicorn, and Uvicorn."
