import requests
import streamlit as st

# Your NewsAPI Key
NEWS_API_KEY = '8dd574348cf74ba6ae6628e7922272fa'

def get_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    news_data = response.json()
    return news_data['articles']

st.title('Preferred Stock News Tracker')

# The keyword for news
query = st.text_input('Enter a keyword for news:', 'Preferred Stock')

if query:
    # Get and display news data
    st.subheader(f'News for "{query}"')
    news_data = get_news(query)
    for article in news_data:
        st.write(f"**{article['title']}**")
        st.write(article['description'])
        st.write(f"[Read more]({article['url']})")
