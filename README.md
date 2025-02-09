# Exirující blog

## Jak spustit (dev)

1 Instalace balíčků

```bash
pip install -r requirements.txt && python manage.py tailwind install
```

2 Inicializace databáze
```bash
python manage.py manage.py migrate
```

2 Příprava skriptu

```bash
chmod +x start-dev.sh
```

4 Spuštění skriptu

```bash
./start-dev.sh
```
