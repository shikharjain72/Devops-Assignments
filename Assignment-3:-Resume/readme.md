# Simple Flask Static App

This project is a minimal Flask application that serves a static HTML page.

## Prerequisites

- Python 3.9+ installed

## Run App (Gunicorn on 8080)

```bash
./run.sh
```

Or manually:

```bash
python3 -m venv "$HOME/.venvs/assignment3_resume"
source "$HOME/.venvs/assignment3_resume/bin/activate"
pip install -r requirements.txt
gunicorn -w 2 -b 0.0.0.0:8080 app:app
```
Open in browser:

- `http://127.0.0.1:8080` (local)
- `http://<EC2_ELASTIC_IP>:8080` (EC2)
