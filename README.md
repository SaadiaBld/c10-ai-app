# 🧠 Application d’analyse de verbatim client (Flask + API IA)

Cette application Flask permet d’envoyer un verbatim client à une API FastAPI protégée, qui l’analyse à l’aide d’un modèle d’intelligence artificielle (Claude 3) pour identifier les **thèmes abordés** et attribuer une **note de satisfaction**.

---

## 🚀 Fonctionnalités

- Interface utilisateur simple et responsive.
- Saisie libre de verbatims clients.
- Appel sécurisé à une API d’analyse IA.
- Affichage des thèmes détectés avec leur note (1 à 5).
- Gestion des erreurs (ex : identifiants invalides, API indisponible).
- Intégration des critères d’**accessibilité** (couleurs, contrastes, structure logique).
- Tests automatisés avec `pytest`.

---

## 🗂️ Structure du projet

```bash
c10-ai-app/
│
├── app/
│ ├── main.py # Script principal Flask
│ └── init.py
│
├── templates/
│ └── index.html # Interface utilisateur
│
├── static/
│ └── style.css # Feuille de style CSS
│
├── tests/
│ └── test_app.py # Tests Flask
│
├── run_test.sh # Script pour lancer les tests
├── requirements.txt # Dépendances Python
└── .env # Variables d’environnement (non versionné)
```
---


## ⚙️ Installation

1. Clone le projet :

```bash
git clone https://github.com/ton-utilisateur/c10-ai-app.git
cd c10-ai-app
```

2. Crée et active un environnement virtuel :

```bash
python -m venv venv
source venv/bin/activate
```

3. Installe les dépendances :

```bash
pip install -r requirements.txt
```

## 🔐 Lancer l'application

Assurez-vous que l’API FastAPI est bien lancée sur http://127.0.0.1:8000.

Puis lance l’app Flask :
```bash
python app/main.py
```
Pour éviter les erreurs de type <<ModuleNotFoundError>>, une autre option est d'utiliser le fichier run_app.sh en le rendant exécutable puis en lançant l'application.

```bash
chmod +x run_app.sh
./run_app.sh
```
L’application est alors disponible sur :
👉 http://127.0.0.1:5000

## ✅ Lancer les tests

```bash
./run_test.sh
```

## 📎 API utilisée

L’application envoie une requête POST au point d’entrée /analyze de l’API FastAPI développée dans la compétence C9.
Cette API nécessite une authentification HTTP Basic.


## 🔒 Sécurité

    Authentification API par identifiant/mot de passe

    Appels sécurisés via requests avec HTTPBasicAuth

    Clés non stockées dans le code, mais dans .env


## Technologies

    Python 3.10

    Flask

    HTML5 / CSS3

    requests

    pytest