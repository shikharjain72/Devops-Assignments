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

## Nginx Setup (Port 80 -> 8080)

Use the project configs in `deploy/nginx/` to avoid invalid Nginx structure errors.

1. Backup existing Nginx config:

```bash
sudo cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak.$(date +%F-%H%M%S)
```

2. Install fixed configs from this project:

```bash
sudo cp deploy/nginx/nginx.conf /etc/nginx/nginx.conf
sudo cp deploy/nginx/resume_app.conf /etc/nginx/conf.d/resume_app.conf
```

3. Validate and restart:

```bash
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl status nginx --no-pager
```

4. Open in browser (without port):

- `http://<EC2_ELASTIC_IP>`
- or your domain on HTTP port 80
