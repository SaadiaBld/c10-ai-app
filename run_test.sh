#!/bin/bash

echo "Lancement des tests Flask avec pytest..."
echo "----------------------------------------"

# Active ton environnement virtuel s’il existe
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Lancer les tests avec couverture si tu veux
pytest tests/ --disable-warnings -v

echo "----------------------------------------"
echo "Tests terminés."
