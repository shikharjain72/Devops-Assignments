#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python app.py

pip install -r requirements.txt


gunicorn -w 2 -b 0.0.0.0:80 app:app
