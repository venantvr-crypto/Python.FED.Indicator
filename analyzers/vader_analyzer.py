# analyzers/vader_analyzer.py
import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class VaderAnalyzer:
    """Analyze text sentiment using NLTK VADER."""

    def __init__(self, url: str):
        """Initialize the analyzer with the target URL."""
        self.url = url
        self.text = None
        self.result = {}

    def _fetch_and_parse_text(self) -> str | None:
        """
        Fetch the text content of a FED press release.
        Returns the text or an error message.
        """
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            html = response.text
            start = html.find("<article")
            end = html.find("</article>") + len("</article>")
            if start == -1 or end == -1:
                return "Error: Unable to find article content in the page."
            article = html[start:end]
            self.text = ' '.join(article.split())
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

        analyzer = SentimentIntensityAnalyzer()
        self.result = analyzer.polarity_scores(self.text)
        return self.result
