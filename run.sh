#!/bin/bash

# NetAudit AutoConfig Runner Script

# Check if virtual environment exists
if [ ! -d "netaudit-env" ]; then
  echo "Creating virtual environment..."
  python3 -m venv netaudit-env
  
  # Activate virtual environment
  source netaudit-env/bin/activate
  
  # Install dependencies
  echo "Installing dependencies..."
  pip install -r requirements.txt
  
  echo "Setup complete!"
else
  # Activate virtual environment
  source netaudit-env/bin/activate
fi

# Run the main application with all provided arguments
python3 netaudit.py "$@"