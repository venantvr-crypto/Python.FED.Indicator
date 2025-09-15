# analyzers/textblob_sentence_analyzer.py
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from textblob import TextBlob


class TextBlobSentenceAnalyzer:
    """Analyze sentiment sentence by sentence with TextBlob."""

    def __init__(self, url: str):
        """Initialize the analyzer with the target URL."""
        self.url = url
        self.text = None
        self.result = {}

    def _fetch_and_parse_text(self) -> str | None:
        """
        Download and extract text from a press release robustly.
        Returns the text or an error message.
        """
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            content_div = soup.find('div', id='pressReleaseText') or soup.find('article')

            if content_div:
                text = ' '.join(p.get_text() for p in content_div.find_all('p'))
            else:
                text = ' '.join(p.get_text() for p in soup.find_all('p'))

            if not text.strip():
                return "Error: Unable to extract meaningful text content."

            self.text = text
            return None  # No error
        except requests.exceptions.RequestException as e:
            return f"Network error or invalid URL: {e}"

    def analyze(self) -> dict:
        """
        Orchestrates the analysis process and returns a dictionary of results.
        """
        error = self._fetch_and_parse_text()
        if error:
            return {"error": error}

        if not self.text:
            return {"error": "The extracted text is empty."}

        sentences = sent_tokenize(self.text)
        if not sentences:
            return {"error": "No sentences could be extracted from the text."}

        total_sentiment = sum(TextBlob(sentence).sentiment.polarity for sentence in sentences)
        average_sentiment = total_sentiment / len(sentences)

        if average_sentiment > 0.05:
            sentiment_label = "Positive"
        elif average_sentiment < -0.05:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

        self.result = {
            "sentiment": sentiment_label,
            "average_polarity": average_sentiment
        }
        return self.result
