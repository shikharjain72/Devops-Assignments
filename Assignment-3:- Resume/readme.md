# Simple Flask Static App

This project is a minimal Flask application that serves a static HTML page.

## Prerequisites

- Python 3.9+ installed

## Run Locally

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

4. Open in browser:

`http://127.0.0.1:5001` (local) or `http://<EC2_ELASTIC_IP>:5001` (EC2)

## Run with Gunicorn (EC2/Production)

1. Ensure dependencies are installed:

```bash
pip install -r requirements.txt
```

2. Start Gunicorn bound to all interfaces:

```bash
gunicorn -w 2 -b 0.0.0.0:5001 app:app
```

3. Open in browser:

`http://<EC2_ELASTIC_IP>:5001`
