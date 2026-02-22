#!/bin/bash


VENV_DIR="${VENV_DIR:-$HOME/.venvs/assignment3_resume}"
PYTHON_BIN="${PYTHON_BIN:-python3}"

echo VENV_DIR="$VENV_DIR"
echo PYTHON_BIN="$PYTHON_BIN"

mkdir -p "$(dirname "$VENV_DIR")"
"$PYTHON_BIN" -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"


# install dependencies
pip install -r requirements.txt

# run the application
gunicorn -w 4 -b 0.0.0.0:8000 app:app &
