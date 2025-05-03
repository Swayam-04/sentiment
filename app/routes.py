from app import app
from flask import render_template, request, jsonify
from app.ai import analyze_sentiment

@app.route('/', methods=['GET'])
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """API endpoint for sentiment analysis"""
    try:
        # Get JSON data from AJAX request
        data = request.get_json()
        text = data.get('text', '')
        
        # Get sentiment from your existing analyze_sentiment function
        sentiment_result = analyze_sentiment(text)
        
        # Return JSON response compatible with the frontend
        return jsonify({
            'success': True,
            'sentiment': sentiment_result.upper(),  # Ensure uppercase (POSITIVE/NEGATIVE/NEUTRAL)
            'polarity': 1.0 if 'POSITIVE' in sentiment_result.upper() else 
                       -1.0 if 'NEGATIVE' in sentiment_result.upper() else 0.0,
            'text': text[:200]  # Return truncated text for reference
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
