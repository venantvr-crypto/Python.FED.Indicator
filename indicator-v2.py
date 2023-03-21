# Importation des bibliothèques
import requests
from textblob import TextBlob


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
blob = TextBlob(text)
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity

# Affichage des résultats
print("Sentiment de l'annonce de la FED :")
if polarity > 0:
    print("Positif")
elif polarity < 0:
    print("Négatif")
else:
    print("Neutre")
print("Polarité :", polarity)
print("Subjectivité :", subjectivity)
