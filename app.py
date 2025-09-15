# app.py
import nltk
from flask import Flask, render_template, request

from analyzers.textblob_document_analyzer import TextBlobDocumentAnalyzer
from analyzers.textblob_sentence_analyzer import TextBlobSentenceAnalyzer
# Importer les classes au lieu des modules
from analyzers.vader_analyzer import VaderAnalyzer

app = Flask(__name__)


def download_nltk_data():
    """Télécharge les données NLTK nécessaires au démarrage."""
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
        analyzer = None
        # Instancier la classe appropriée en fonction de l'indicateur
        if indicator == 'v1':
            analyzer = VaderAnalyzer(url=url)
        elif indicator == 'v2':
            analyzer = TextBlobDocumentAnalyzer(url=url)
        elif indicator == 'v3':
            analyzer = TextBlobSentenceAnalyzer(url=url)
        else:
            error = "Indicateur de sentiment invalide."

        if analyzer:
            # Appeler la méthode .analyze()
            result = analyzer.analyze()
            if 'error' in result:
                error = result.pop('error')  # Récupérer l'erreur et la retirer du résultat

    except Exception as e:
        error = f"Une erreur inattendue est survenue : {e}"
        result = None

    return render_template('index.html', result=result, error=error, indicator=indicator, submitted_url=url)


if __name__ == '__main__':
    app.run(debug=True)