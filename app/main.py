from flask import Flask, render_template, request
import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

app = Flask(__name__, static_folder="../static", template_folder="../templates")

load_dotenv()
API_USER= os.getenv("API_USER")
API_PASS=os.getenv("API_PASS")

API_URL = "http://127.0.0.1:8000/analyze"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    verbatim = ""

    if request.method == "POST":
        verbatim = request.form.get("verbatim", "")
        try:
            response = requests.post(
                API_URL,
                json={"text": verbatim},
                auth=HTTPBasicAuth(API_USER, API_PASS)
            )
            if response.status_code == 200:
                result = response.json()
            else:
                error = f"Erreur API ({response.status_code}) : {response.json().get('detail')}"
        except Exception as e:
            error = f"Erreur lors de la requête : {str(e)}"

    return render_template("index.html", result=result, error=error, verbatim=verbatim)
