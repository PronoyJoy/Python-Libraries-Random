from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment(text):
    """
    Analyze the sentiment of the input text.
    
    :param text: The text to analyze
    :return: Polarity and Subjectivity scores
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # -1 (negative) to 1 (positive)
    subjectivity = blob.sentiment.subjectivity  # 0 (objective) to 1 (subjective)
    
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "Text": text,
        "Polarity": polarity,
        "Subjectivity": subjectivity,
        "Sentiment": sentiment,
    }

# Example usage
if __name__ == "__main__":
    text_input = input("Enter a sentence for sentiment analysis: ")
    result = analyze_sentiment(text_input)
    print("\nSentiment Analysis Result:")
    for key, value in result.items():
        print(f"{key}: {value}")
