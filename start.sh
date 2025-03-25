#!/bin/bash

cd /home/kristian.kunc/2024_WA_INF1_kunc_python
source venv/bin/activate

pip install -r requirements.txt
manage.py tailwind install

python manage.py migrate

python manage.py tailwind build