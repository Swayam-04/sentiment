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

Set start command: gunicorn app:app

To Heroku:
bash
heroku create
git push heroku main
heroku open
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

Gunicorn (for production)

License
MIT License - See LICENSE for details.


### Key Features of This README:
1. **Badges** - Visual indicators for technologies used
2. **Clear Sections** - Installation, Usage, Deployment separated
3. **Code Formatting** - Proper markdown code blocks
4. **Visual Structure** - Directory tree visualization
5. **API Documentation** - Clear endpoint specification
6. **Deployment Guides** - For both Render and Heroku

To use:
1. Save this as `README.md` in your project root
2. Replace `EXAMPLE_SCREENSHOT.png` with an actual screenshot
3. Update any version numbers if needed
4. Add your own LICENSE file if using something other than MIT

Would you like me to add any additional sections like:
- Contribution guidelines
- Troubleshooting tips
- Roadmap/features planned
- More detailed API documentation?
