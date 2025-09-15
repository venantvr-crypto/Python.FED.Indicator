# app.py
import nltk
from flask import Flask, render_template, request

from analyzers.textblob_document_analyzer import TextBlobDocumentAnalyzer
from analyzers.textblob_sentence_analyzer import TextBlobSentenceAnalyzer
# Import classes instead of modules
from analyzers.vader_analyzer import VaderAnalyzer

app = Flask(__name__)


def download_nltk_data():
    """Download necessary NLTK data at startup."""
    try:
        nltk.data.find('sentiment/vader_lexicon.zip')
        print("✅ VADER lexicon is already downloaded.")
    except LookupError:
        print("📥 Downloading VADER lexicon...")
        nltk.download('vader_lexicon')
    try:
        nltk.data.find('tokenizers/punkt')
        print("✅ Punkt tokenizer is already downloaded.")
    except LookupError:
        print("📥 Downloading Punkt tokenizer...")
        nltk.download('punkt')


download_nltk_data()


@app.route('/')
def index():
    """Display the homepage."""
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    """Handle the analysis form submission."""
    url = request.form.get('url')
    indicator = request.form.get('indicator')

    if not url or not url.startswith('http'):
        return render_template('index.html', error="A valid URL is required.", indicator=indicator, submitted_url=url)

    result = None
    error = None

    try:
        analyzer = None
        # Instantiate the appropriate class based on the indicator
        if indicator == 'v1':
            analyzer = VaderAnalyzer(url=url)
        elif indicator == 'v2':
            analyzer = TextBlobDocumentAnalyzer(url=url)
        elif indicator == 'v3':
            analyzer = TextBlobSentenceAnalyzer(url=url)
        else:
            error = "Invalid sentiment indicator."

        if analyzer:
            # Call the .analyze() method
            result = analyzer.analyze()
            if 'error' in result:
                error = result.pop('error')  # Retrieve the error and remove it from the result

    except Exception as e:
        error = f"An unexpected error occurred: {e}"
        result = None

    return render_template('index.html', result=result, error=error, indicator=indicator, submitted_url=url)


if __name__ == '__main__':
    app.run(debug=True)
