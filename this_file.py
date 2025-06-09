# News Sentiment Analyzer Project
# Dependencies: requests, textblob, streamlit

import requests
from textblob import TextBlob
import streamlit as st

# --- Streamlit UI Setup --- #
st.title("📰 News Sentiment Analyzer")
st.write("Analyze the sentiment of today's headlines based on a keyword.")

# --- User Input --- #
query = st.text_input("Enter keyword (e.g., technology, sports, politics):", "technology")
api_key = "0c43df05beae4c07a2b31b4f095d4fab"  # <-- Replace this with your NewsAPI.org key

# --- Function to Fetch News --- #
def fetch_news(query, api_key):
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&pageSize=10&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        st.error("Failed to fetch news. Check your API key and internet connection.")
        return []
    return response.json().get("articles", [])

# --- Function to Analyze Sentiment --- #
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

# --- Display Results --- #
if st.button("Analyze News"): 
    with st.spinner("Fetching and analyzing news..."):
        articles = fetch_news(query, api_key)
        if not articles:
            st.warning("No articles found.")
        else:
            for article in articles:
                title = article.get("title", "No Title")
                polarity = analyze_sentiment(title)
                sentiment = "🟢 Positive" if polarity > 0 else ("🔴 Negative" if polarity < 0 else "🟡 Neutral")
                st.write(f"**{title}**\n- Sentiment: {sentiment} ({round(polarity, 2)})")

# --- How to Run --- #
# 1. pip install streamlit textblob requests
# 2. python -m textblob.download_corpora
# 3. Run using: streamlit run this_file.py
