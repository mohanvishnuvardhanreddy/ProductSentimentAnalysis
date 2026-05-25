from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def compute_sentiment(text):
    # Get score metrics
    scores = sia.polarity_scores(text)
    compound_score = scores['compound']
    
    # Classify based on standard thresholds
    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'