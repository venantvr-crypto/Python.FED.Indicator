# indicator_v3.py
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from textblob import TextBlob


def telecharger_annonce_v3(url):
    """Télécharge et extrait le texte d'un communiqué de manière robuste."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Essayer de trouver le contenu de plusieurs manières
        content_div = soup.find('div', id='pressReleaseText') or soup.find('article')

        if content_div:
            texte = ' '.join(p.get_text() for p in content_div.find_all('p'))
        else:
            texte = ' '.join(p.get_text() for p in soup.find_all('p'))

        if not texte.strip():
            return "Erreur : Impossible d'extraire un contenu textuel significatif de la page."

        return texte
    except requests.exceptions.RequestException as e:
        return f"Erreur de réseau ou URL invalide : {e}"


def run_indicator_v3(url):
    """Exécute l'analyse en moyennant le sentiment de chaque phrase."""
    texte_annonce = telecharger_annonce_v3(url)
    if texte_annonce.startswith("Erreur"):
        return {"error": texte_annonce}

    phrases = sent_tokenize(texte_annonce)
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

    return {
        "sentiment": sentiment_label,
        "average_polarity": sentiment_moyen
    }
