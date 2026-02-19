#!/bin/bash

# venv cannot be created under this project path because it contains ":".
# Use a safe default path outside the workspace; allow override via VENV_DIR.
VENV_DIR="${VENV_DIR:-$HOME/.venvs/assignment3_resume}"
PYTHON_BIN="${PYTHON_BIN:-python3}"
mkdir -p "$(dirname "$VENV_DIR")"
"$PYTHON_BIN" -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

python3 -m pip install -r requirements.txt
python3 -m pip install gunicorn

exec gunicorn --bind 0.0.0.0:8080 app:app

