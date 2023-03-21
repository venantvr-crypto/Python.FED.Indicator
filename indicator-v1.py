# Importation des bibliothèques
import nltk
import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Fonction pour récupérer le texte d'une annonce de la FED
def get_fed_announcement(feed_url):
    response = requests.get(feed_url)
    html = response.text
    start = html.find("<article")
    end = html.find("</article>") + len("</article>")
    article = html[start:end]
    output = article.replace("\n", " ")
    return output


# URL de l'annonce de la FED
url = "https://www.federalreserve.gov/newsevents/pressreleases/monetary20220316a.htm"

# Récupération du texte de l'annonce
text = get_fed_announcement(url)

# Analyse du sentiment
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()
sentiment = analyzer.polarity_scores(text)

# Affichage des résultats
print("Sentiment de l'annonce de la FED :")
print("Positif :", sentiment["pos"])
print("Neutre :", sentiment["neu"])
print("Négatif :", sentiment["neg"])
