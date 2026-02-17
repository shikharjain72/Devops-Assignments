#!/bin/bash
set -e

# venv cannot be created under this project path because it contains ":".
# Use a safe default path outside the workspace; allow override via VENV_DIR.
VENV_DIR="${VENV_DIR:-$HOME/.venvs/assignment3_resume}"
mkdir -p "$(dirname "$VENV_DIR")"
python3.11 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

pip install -r requirements.txt

PORT="${PORT:-8080}"

exec gunicorn -w 2 -b "0.0.0.0:${PORT}" app:app
