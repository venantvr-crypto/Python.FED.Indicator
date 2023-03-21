import nltk
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from textblob import TextBlob


# Télécharger l'annonce de la FED
def telecharger_annonce(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    texte = ' '.join(p.get_text() for p in soup.find_all('p'))
    return texte


# Analyser le sentiment d'un texte
def analyser_sentiment(texte):
    sentiment_total = 0
    nb_phrases = 0

    nltk.download("punkt")

    phrases = sent_tokenize(texte)
    for phrase in phrases:
        blob = TextBlob(phrase)
        sentiment_total += blob.sentiment.polarity
        nb_phrases += 1

    sentiment_moyen = sentiment_total / nb_phrases
    return sentiment_moyen


# Exemple d'utilisation
url_annonce = "https://www.federalreserve.gov/monetarypolicy/fomc.htm"
# Remplacer par l'URL de l'annonce de la FED
texte_annonce = telecharger_annonce(url_annonce)
sentiment = analyser_sentiment(texte_annonce)

if sentiment > 0:
    print(f"Sentiment positif : {sentiment:.2f}")
elif sentiment < 0:
    print(f"Sentiment négatif : {sentiment:.2f}")
else:
    print("Sentiment neutre")
