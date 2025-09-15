# FED Announcement Sentiment Analysis

A web application for analyzing the sentiment of Federal Reserve (FED) press releases and announcements. This application provides a user-friendly interface
to run three distinct sentiment analysis algorithms on any FED announcement URL.

## Features

- **Intuitive Web Interface**: A clean and simple user interface built with Flask and Bootstrap.
- **Multiple Analysis Models**: Choose from three sentiment analysis indicators:
    - **Indicator v1**: Uses NLTK VADER, a robust lexicon-based model optimized for sentiment.
    - **Indicator v2**: Employs TextBlob for quick polarity and subjectivity calculation of the entire text.
    - **Indicator v3**: A more granular approach that calculates the average sentiment of each individual sentence with TextBlob.
- **Detailed Results**: View sentiment scores directly in the web interface.
- **Simple Deployment**: Runs locally as a standard Flask application.

## Installation

Follow these steps to set up and run the project on your machine.

### 1. Prerequisites

- Python 3.7+
- `pip` package manager

### 2. Clone the Repository

Clone this repository to your local machine:

```bash
git clone <repository_url>
cd <project_directory>
```

### 3. Create a Virtual Environment (Recommended)

For clean dependency management, create and activate a virtual environment.

- **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

### 4. Install Dependencies

Install the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

On first launch, the application will also automatically download the necessary NLTK data (`vader_lexicon` and `punkt`).

## Usage

### 1. Start the Flask Server

Run the `app.py` file to launch the local web server.

```bash
python app.py
```

The terminal will indicate that the server is running, typically at `http://127.0.0.1:5000`.

### 2. Access the Web Interface

Open your web browser and go to:
[**http://127.0.0.1:5000**](http://127.0.0.1:5000)

### 3. Perform an Analysis

1. **Choose an Indicator**: Select the "Indicator v1", "v2", or "v3" tab.
2. **Enter a URL**: Find a press release URL from the [Federal Reserve website](https://www.federalreserve.gov/newsevents/pressreleases.htm) and paste it in the input
   field.

- *Example URL:* `https://www.federalreserve.gov/newsevents/pressreleases/monetary20230503a.htm`

3. **Analyze**: Click the "Analyze Sentiment" button.
4. **Review Results**: The page will reload to display the detailed analysis results.