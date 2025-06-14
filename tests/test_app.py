import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app
from unittest.mock import patch


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """
    Vérifie que la page d'accueil se charge bien.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"Analyse de verbatim client" in response.data

def test_post_valid_verbatim(client):
    """
    Vérifie qu'un verbatim valide est accepté et que la réponse contient un résultat ou une erreur gérée.
    """
    data = {
        "verbatim": "Livraison catastrophique, colis arrivé en retard et abîmé"
    }

    response = client.post("/", data=data)
    assert response.status_code == 200
    assert "Résultat" in response.get_data(as_text=True) or "Erreur" in response.get_data(as_text=True)

def test_post_empty_verbatim(client):
    """
    Vérifie qu'un verbatim vide retourne une erreur claire (validation côté API).
    """
    data = {"verbatim": ""}
    response = client.post("/", data=data)
    assert response.status_code == 200
    content = response.get_data(as_text=True)
    assert "Erreur" in content or "échec" in content.lower()

@patch("app.main.requests.post")
def test_api_failure_handling(mock_post, client):
    """
    Simule une erreur lors de l'appel à l'API et vérifie que l'application gère le problème.
    """
    mock_post.side_effect = Exception("API KO")
    data = {"verbatim": "Un problème très grave est survenu"}
    response = client.post("/", data=data)
    assert response.status_code == 200
    content = response.get_data(as_text=True)
    assert "Erreur" in content
