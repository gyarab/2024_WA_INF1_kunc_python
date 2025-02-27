# Exirující blog

Blog, který automaticky maže nudné články.

## Jak spustit (dev)

1. Instalace balíčků

```bash
pip install -r requirements.txt && python manage.py tailwind install
```

2. Inicializace databáze

```bash
python manage.py migrate
```

3. Nahrání ukázkových dat

```bash
python manage.py loaddata init.json
```

4. Kompilace tailwind stylů

```bash
python manage.py tailwind build
```

5. Spuštění vývojového serveru

```bash
python manage.py runserver
```
