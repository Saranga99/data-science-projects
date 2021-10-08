import pickle
import streamlit as st
# convert text in to feature vectors
from sklearn.feature_extraction.text import TfidfVectorizer


#header and description
st.title("Fake News Classifier")
st.write("This Application will Classify news into fake or true")
# loading the trained model
pickle_in = open('log_reg.pkl', 'rb')
classifier = pickle.load(pickle_in)


@st.cache()
# defining the function which will make the prediction using the data which the user inputs
def prediction(text):
    # ocnverting data to numerical data
    vectorizer = TfidfVectorizer()
    text = vectorizer.fit_transform(text)
    prediction = classifier.predict([[text]])
    st.write(prediction)


news = st.text_input("Please Type your News here")
# button
button = st.button("Ckeck")


with st.spinner("Discovering Answers.."):
    # used try catch because not neccery to show errors in gui
    if button:
        prediction(news)
