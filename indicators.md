# FED Announcement Sentiment Analysis Indicators

This document combines three different approaches to analyze the sentiment of Federal Reserve (FED) announcements using Python and various Natural Language Processing (
NLP) libraries.

## Indicator v1: NLTK VADER Sentiment Analysis

### Overview

This indicator uses NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analyzer, which is specifically designed for social media text but works well
with financial communications.

### Implementation

```python
# Import libraries
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import requests


# Function to retrieve FED announcement text
def get_fed_announcement(url):
    response = requests.get(url)
    html = response.text
    start = html.find("<article")
    end = html.find("</article>") + len("</article>")
    article = html[start:end]
    text = article.replace("\n", " ")
    return text


# FED announcement URL
url = "https://www.federalreserve.gov/newsevents/pressreleases/monetary20220316a.htm"

# Retrieve announcement text
text = get_fed_announcement(url)

# Sentiment analysis
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()
sentiment = analyzer.polarity_scores(text)

# Display results
print("FED Announcement Sentiment:")
print("Positive:", sentiment["pos"])
print("Neutral:", sentiment["neu"])
print("Negative:", sentiment["neg"])
```

### Key Features

- Uses VADER lexicon-based sentiment analysis
- Provides separate scores for positive, neutral, and negative sentiment
- Effective for quick sentiment assessment

### Limitations

- Provides only raw sentiment analysis
- Can be improved with more advanced machine learning techniques

## Indicator v2: TextBlob Document-Level Analysis

### Overview

This indicator uses TextBlob API to analyze the overall sentiment of the entire FED announcement document.

### Implementation

```python
# Import libraries
import requests
from textblob import TextBlob


# Function to retrieve FED announcement text
def get_fed_announcement(url):
    response = requests.get(url)
    html = response.text
    start = html.find("<article")
    end = html.find("</article>") + len("</article>")
    article = html[start:end]
    text = article.replace("\n", " ")
    return text


# FED announcement URL
url = "https://www.federalreserve.gov/newsevents/pressreleases/monetary20220316a.htm"

# Retrieve announcement text
text = get_fed_announcement(url)

# Sentiment analysis
blob = TextBlob(text)
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity

# Display results
print("FED Announcement Sentiment:")
if polarity > 0:
    print("Positive")
elif polarity < 0:
    print("Negative")
else:
    print("Neutral")
print("Polarity:", polarity)
print("Subjectivity:", subjectivity)
```

### Key Features

- Analyzes entire document as a single unit
- Provides polarity (-1 to 1) and subjectivity (0 to 1) scores
- Simple and fast implementation

## Indicator v3: TextBlob Sentence-Level Analysis

### Overview

This indicator provides a more granular approach by analyzing sentiment at the sentence level and averaging the results.

### Implementation

```python
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from textblob import TextBlob
import nltk

nltk.download("punkt")


# Download FED announcement
def download_announcement(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = ' '.join(p.get_text() for p in soup.find_all('p'))
    return text


# Analyze text sentiment
def analyze_sentiment(text):
    total_sentiment = 0
    sentence_count = 0

    sentences = sent_tokenize(text)
    for sentence in sentences:
        blob = TextBlob(sentence)
        total_sentiment += blob.sentiment.polarity
        sentence_count += 1

    average_sentiment = total_sentiment / sentence_count
    return average_sentiment


# Example usage
announcement_url = "https://www.example.com/fed_announcement"  # Replace with actual FED announcement URL
announcement_text = download_announcement(announcement_url)
sentiment = analyze_sentiment(announcement_text)

if sentiment > 0:
    print(f"Positive sentiment: {sentiment:.2f}")
elif sentiment < 0:
    print(f"Negative sentiment: {sentiment:.2f}")
else:
    print("Neutral sentiment")
```

### Key Features

- Sentence-by-sentence analysis for more accurate sentiment assessment
- Calculates average sentiment across all sentences
- Uses BeautifulSoup for better HTML parsing

### Required Dependencies

```bash
pip install requests beautifulsoup4 nltk textblob
```

### Troubleshooting

If you encounter "Resource punkt not found" error, ensure you download the punkt tokenizer:

```python
import nltk

nltk.download("punkt")
```

## Accessing FED Announcements

### Official FED Resources

1. **Federal Reserve Board (FOMC) - Calendar and Communications:**
   https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm

2. **FOMC - Meeting Minutes:**
   https://www.federalreserve.gov/monetarypolicy/fomcminutes.htm

3. **FOMC - Statements:**
   https://www.federalreserve.gov/monetarypolicy/fomc.htm

4. **FOMC - Transcripts and Historical Documents:**
   https://www.federalreserve.gov/monetarypolicy/fomc_historical.htm

### RSS Feed

Access the FED's RSS feed for automatic updates:
https://www.federalreserve.gov/feeds/press_all.xml

## Additional Data Sources

### News APIs and Services

For broader sentiment analysis, you can integrate news articles from various sources:

#### Free API Options

1. **Google News API**
    - Limited daily requests
    - Access to recent news from various sources
    - Some advanced features may be restricted

2. **Reuters News API**
    - Free tier: up to 500 requests per day
    - Access to subset of articles
    - Data may be delayed compared to paid version

3. **Bloomberg API**
    - Free tier: up to 500 requests per month
    - Limited market data and news feeds
    - Not all market data available

4. **Financial Times API**
    - Free tier: up to 100 requests per day
    - Limited access to articles and market data
    - Reduced functionality compared to paid version

### Financial Analysis Resources

- **Google News:** Search for recent economic and financial events
- **Reuters:** International news agency covering financial news
- **Bloomberg:** Financial information and market analysis
- **Financial Times:** Global business and economic news
- **Investing.com Technical Analysis:** https://www.investing.com/analysis/technical-analysis

## Best Practices

1. **Combine Multiple Indicators:** Use all three sentiment indicators for a more comprehensive analysis
2. **Consider Context:** FED language is often nuanced; consider the broader economic context
3. **Validate Results:** Cross-reference sentiment scores with market reactions and expert analysis
4. **Update Regularly:** FED communication patterns may change; regularly update your analysis methods

## Limitations and Disclaimers

- Machine learning-based sentiment analysis is not perfect and may produce inaccurate results
- Short-term market predictions carry high uncertainty and risk
- Always conduct thorough research and consider multiple information sources before making investment decisions
- These algorithms provide raw sentiment analysis that should be part of a broader analytical framework