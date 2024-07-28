import streamlit as st
from textblob import TextBlob

# Sentiment Analysis Function
def analyze_sentiment(text):
   
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0:
        return "Positive"
    elif blob.sentiment.polarity==0:
        return "Neutral"
    else:
        return "Negative"

# Streamlit App
def main():
    st.title("Sentiment Analysis Tool")
    text = st.text_input("Enter a sentence:")
    if st.button("Analyze Sentiment"):
        sentiment = analyze_sentiment(text)
        st.write(f"The sentiment of the text is: {sentiment}")
        blob = TextBlob(text)
        

if __name__ == "__main__":
    main()