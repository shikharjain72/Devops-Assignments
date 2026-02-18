# Simple Flask Static App

This project is a minimal Flask application that serves a static HTML page.

Refactored commands with brief inline comments:

```bash
# Create a dedicated virtual environment for this project
python3 -m venv "$HOME/.venvs/assignment3_resume"

# Activate the virtual environment (bash/zsh). On Windows use the equivalent activate script.
source "$HOME/.venvs/assignment3_resume/bin/activate"

# Install project dependencies listed in requirements.txt into the active venv
pip install -r requirements.txt

# Start the Flask app using Gunicorn:
# -w 2 : use 2 worker processes
# -b 0.0.0.0:8080 : bind to all interfaces on port 8080
# app:app : module `app`, Flask app object `app`
gunicorn -w 2 -b 0.0.0.0:8080 app:app
```

Open in browser:

- `http://127.0.0.1:8080` (local)
- `http://<EC2_ELASTIC_IP>:8080` (EC2)
