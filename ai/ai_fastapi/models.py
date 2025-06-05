from transformers import pipeline

def get_sentiment_model():
    return pipeline('sentiment-analysis')
