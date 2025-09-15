# indicator_v1.py
import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_fed_announcement_v1(url):
    """Récupère le contenu textuel d'un communiqué de la FED."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html = response.text
        start = html.find("<article")
        end = html.find("</article>") + len("</article>")
        if start == -1 or end == -1:
            return "Erreur : Impossible de trouver le contenu de l'article dans la page."
        article = html[start:end]
        output = ' '.join(article.split())
        return output
    except requests.exceptions.RequestException as e:
        return f"Erreur de réseau ou URL invalide : {e}"


def run_indicator_v1(url):
    """Exécute l'analyse de sentiment avec NLTK VADER."""
    text = get_fed_announcement_v1(url)
    if text.startswith("Erreur"):
        return {"error": text}

    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    return sentiment
