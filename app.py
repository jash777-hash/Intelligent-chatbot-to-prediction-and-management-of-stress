import streamlit as st
from textblob import TextBlob

# Function to analyze sentiment
def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive 😊"
    elif sentiment < 0:
        return "Negative 😠"
    else:
        return "Neutral 😐"

# Streamlit app layout
st.title("Sentiment Analysis App")

user_input = st.text_area("Enter Text Data")

if st.button("Analyze"):
    if user_input:
        sentiment_result = get_sentiment(user_input)
        st.write(f"**Sentiment:** {sentiment_result}")
    else:
        st.warning("⚠️ Please enter some text data.")
