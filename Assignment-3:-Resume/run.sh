#!/bin/bash
set -e

# venv cannot be created under this project path because it contains ":".
# Use a safe default path outside the workspace; allow override via VENV_DIR.
VENV_DIR="${VENV_DIR:-$HOME/.venvs/assignment3_resume}"
PYTHON_BIN="${PYTHON_BIN:-python3}"
mkdir -p "$(dirname "$VENV_DIR")"
"$PYTHON_BIN" -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

pip install -r requirements.txt

PORT="${PORT:-8080}"

if command -v lsof >/dev/null 2>&1; then
  IN_USE_PID="$(lsof -t -iTCP:"$PORT" -sTCP:LISTEN 2>/dev/null | head -n 1)"
  if [ -n "$IN_USE_PID" ]; then
    if [ "${AUTO_KILL_PORT:-0}" = "1" ]; then
      echo "Port $PORT is in use by PID $IN_USE_PID. Stopping it..."
      kill "$IN_USE_PID"
      sleep 1
    else
      echo "Port $PORT is already in use by PID $IN_USE_PID."
      echo "Stop it first: kill $IN_USE_PID"
      echo "Or rerun with AUTO_KILL_PORT=1 to stop it automatically."
      exit 1
    fi
  fi
fi

exec gunicorn -w 2 -b "0.0.0.0:${PORT}" app:app
