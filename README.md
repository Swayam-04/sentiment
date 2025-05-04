# Sentiment Analysis Web App

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.3.2-lightgrey.svg)
![TextBlob](https://img.shields.io/badge/textblob-0.17.1-yellowgreen.svg)

A web application that analyzes text sentiment using Natural Language Processing (NLP) with Flask and TextBlob.

## Features

- Real-time sentiment analysis (Positive/Negative/Neutral)
- Clean, responsive UI with modern styling
- RESTful API endpoint for programmatic access
- Easy deployment to Render/Heroku

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Swayam-04/sentiment.git
   cd sentiment
Create and activate virtual environment:

python -m venv venv
venv\Scripts\activate     # Windows

Install dependencies:

pip install -r requirements.txt
python -m textblob.download_corpora

Usage
Run the development server:

python run.py
Access the web interface at http://localhost:5000

API Endpoint
Send POST requests to /analyze with JSON:

json
{
  "text": "Your text to analyze"
}
Deployment
To Render:
Create new Web Service

Set build command: pip install -r requirements.txt

Project Structure
sentiment/
├── app/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   └── routes.py
├── requirements.txt
├── Procfile
└── runtime.txt

Dependencies
Flask 2.3.2
TextBlob 0.17.1
Werkzeug 2.3.7

License
MIT License - See LICENSE for details.
