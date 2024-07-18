import streamlit as st
import pickle

# Define your data cleaning function
def text_data_cleaning(text):
    # Implement your text cleaning logic here
    cleaned_text = text.strip().lower()  # Example cleaning logic
    return cleaned_text

# Load your pre-trained sentiment analysis model
with open('D:\sentemet analysis app\ifan_IMDB_model.pkl', 'rb') as f:
    clf = pickle.load(f)

# Streamlit app layout
st.title("Sentiment Analysis App by irfan")
st.write("Enter a sentence to analyze its sentiment")

# Function to preprocess input text and predict sentiment
def predict_sentiment(text):
    cleaned_text = text_data_cleaning(text)  # Clean the input text
    prediction = clf.predict([cleaned_text])[0]  # Pass the cleaned text to the model
    sentiment = 'Positive' if prediction == 1 else 'Negative'
    return sentiment

# Streamlit app layout continued
# Input text box
user_input = st.text_area("Enter your sentence here:")

if st.button("Analyze"):
    if user_input:
        # Get the sentiment prediction
        sentiment = predict_sentiment(user_input)
        # Display the result
        st.write(f"Sentiment: **{sentiment}**")
    else:
        st.write("Please enter a sentence to analyze.")

# Additional information
st.write("This app uses a pre-trained sentiment analysis model to classify the sentiment of the entered text as Positive or Negative.")
