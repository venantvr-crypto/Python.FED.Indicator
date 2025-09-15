# analyzers/textblob_document_analyzer.py
import requests
from textblob import TextBlob


class TextBlobDocumentAnalyzer:
    """Analyse le sentiment du document entier avec TextBlob."""

    def __init__(self, url: str):
        """Initialise l'analyseur avec l'URL cible."""
        self.url = url
        self.text = None
        self.result = {}

    def _fetch_and_parse_text(self) -> str | None:
        """
        Récupère le contenu textuel d'un communiqué de la FED.
        Retourne le texte ou un message d'erreur.
        """
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            html = response.text
            start = html.find("<article")
            end = html.find("</article>") + len("</article>")
            if start == -1 or end == -1:
                return "Erreur : Impossible de trouver le contenu de l'article dans la page."
            article = html[start:end]
            self.text = ' '.join(article.split())
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

        blob = TextBlob(self.text)
        polarity = blob.sentiment.polarity

        if polarity > 0.05:
            sentiment_label = "Positif"
        elif polarity < -0.05:
            sentiment_label = "Négatif"
        else:
            sentiment_label = "Neutre"

        self.result = {
            "sentiment": sentiment_label,
            "polarity": polarity,
            "subjectivity": blob.sentiment.subjectivity
        }
        return self.result
