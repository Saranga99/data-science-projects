import pickle
import streamlit as st
# convert text in to feature vectors
from sklearn.feature_extraction.text import TfidfVectorizer
import re #usful for searching words in pharagraph
from nltk.corpus import stopwords  #words doesn't add much value to phara (rticals)
from nltk.stem.porter import PorterStemmer #gives a root word
from sklearn.feature_extraction.text import TfidfVectorizer #convert text in to feature vectors


def stemming(content):
    port_stem=PorterStemmer()
    stemmed_content=re.sub("[^a-zA-z]"," ",content)
    stemmed_content=stemmed_content.lower()
    stemmed_content=stemmed_content.split()
    stemmed_content=[port_stem.stem(word) for word in stemmed_content if not word in stopwords.words("english")]
    stemmed_content= " ".join(stemmed_content)
    return stemmed_content

#header and description
st.title("Fake News Classifier")
st.write("This Application will Classify news into fake or true")
# loading the trained model
pickle_in = open('log_reg.pkl', 'rb')
classifier = pickle.load(pickle_in)


@st.cache()
# defining the function which will make the prediction using the data which the user inputs
def prediction(text):
    text=text.apply(stemming)
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
