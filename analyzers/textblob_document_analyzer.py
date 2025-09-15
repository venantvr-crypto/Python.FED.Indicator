# indicator_v2.py
import requests
from textblob import TextBlob


def get_fed_announcement_v2(url):
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


def run_indicator_v2(url):
    """Exécute l'analyse de sentiment avec TextBlob."""
    text = get_fed_announcement_v2(url)
    if text.startswith("Erreur"):
        return {"error": text}

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0.05:
        sentiment_label = "Positif"
    elif polarity < -0.05:
        sentiment_label = "Négatif"
    else:
        sentiment_label = "Neutre"

    return {
        "sentiment": sentiment_label,
        "polarity": polarity,
        "subjectivity": subjectivity
    }
