trap 'kill $(jobs -p)' EXIT
python manage.py tailwind start & 
python manage.py runserver