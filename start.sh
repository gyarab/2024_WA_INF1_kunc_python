#!/bin/bash
source .venv/bin/activate
python3 manage.py tailwind build
exec python3 manage.py runserver 0.0.0.0:35903
