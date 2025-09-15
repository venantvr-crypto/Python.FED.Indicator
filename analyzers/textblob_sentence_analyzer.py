# analyzers/textblob_sentence_analyzer.py
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from textblob import TextBlob


class TextBlobSentenceAnalyzer:
    """Analyse le sentiment phrase par phrase avec TextBlob."""

    def __init__(self, url: str):
        """Initialise l'analyseur avec l'URL cible."""
        self.url = url
        self.text = None
        self.result = {}

    def _fetch_and_parse_text(self) -> str | None:
        """
        Télécharge et extrait le texte d'un communiqué de manière robuste.
        Retourne le texte ou un message d'erreur.
        """
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            content_div = soup.find('div', id='pressReleaseText') or soup.find('article')

            if content_div:
                texte = ' '.join(p.get_text() for p in content_div.find_all('p'))
            else:
                texte = ' '.join(p.get_text() for p in soup.find_all('p'))

            if not texte.strip():
                return "Erreur : Impossible d'extraire un contenu textuel significatif."

            self.text = texte
            return None  # Pas d'erreur
        except requests.exceptions.RequestException as e:
            return f"Erreur de réseau ou URL invalide : {e}"

    def analyze(self) -> dict:
        """
        Orchestre le processus d'analyse et retourne un dictionnaire de résultats.
        """
        error = self._fetch_and_parse_text()
        if error:
            return {"error": error}

        if not self.text:
            return {"error": "Le texte extrait est vide."}

        phrases = sent_tokenize(self.text)
        if not phrases:
            return {"error": "Aucune phrase n'a pu être extraite du texte."}

        sentiment_total = sum(TextBlob(phrase).sentiment.polarity for phrase in phrases)
        sentiment_moyen = sentiment_total / len(phrases)

        if sentiment_moyen > 0.05:
            sentiment_label = "Positif"
        elif sentiment_moyen < -0.05:
            sentiment_label = "Négatif"
        else:
            sentiment_label = "Neutre"

        self.result = {
            "sentiment": sentiment_label,
            "average_polarity": sentiment_moyen
        }
        return self.result
