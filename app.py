# app.py
import nltk
from flask import Flask, render_template, request

import indicator_v1 as v1
import indicator_v2 as v2
import indicator_v3 as v3

app = Flask(__name__)


def download_nltk_data():
    """
    Télécharge les données NLTK nécessaires au démarrage.
    Utilise LookupError qui est la méthode correcte pour les versions récentes de NLTK.
    """
    try:
        nltk.data.find('sentiment/vader_lexicon.zip')
        print("✅ Le lexique VADER est déjà téléchargé.")
    except LookupError:
        print("📥 Téléchargement du lexique VADER...")
        nltk.download('vader_lexicon')
    try:
        nltk.data.find('tokenizers/punkt')
        print("✅ Le tokenizer Punkt est déjà téléchargé.")
    except LookupError:
        print("📥 Téléchargement du tokenizer Punkt...")
        nltk.download('punkt')


# Télécharger les données au lancement de l'application
download_nltk_data()


@app.route('/')
def index():
    """Affiche la page d'accueil."""
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    """Gère la soumission du formulaire d'analyse."""
    url = request.form.get('url')
    indicator = request.form.get('indicator')

    if not url or not url.startswith('http'):
        return render_template('index.html', error="Une URL valide est requise.", indicator=indicator, submitted_url=url)

    result = None
    error = None

    try:
        if indicator == 'v1':
            result = v1.run_indicator_v1(url)
        elif indicator == 'v2':
            result = v2.run_indicator_v2(url)
        elif indicator == 'v3':
            result = v3.run_indicator_v3(url)
        else:
            error = "Indicateur de sentiment invalide."

        if result and 'error' in result:
            error = result['error']
            result = None

    except Exception as e:
        error = f"Une erreur inattendue est survenue : {e}"

    return render_template('index.html', result=result, error=error, indicator=indicator, submitted_url=url)


if __name__ == '__main__':
    app.run(debug=True)
