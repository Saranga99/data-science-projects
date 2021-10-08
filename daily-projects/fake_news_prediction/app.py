import pickle
import streamlit as st


#header and description
st.title("Fake News Classifier")
st.write("This Application will Classify news into fake or true")
# loading the trained model
pickle_in = open('log_reg.pkl', 'rb')
classifier = pickle.load(pickle_in)


@st.cache()
# defining the function which will make the prediction using the data which the user inputs
def prediction(text):
    prediction = classifier.predict([[text]])
    st.write(prediction)


news = st.text_input("Please Type your News here")
# button
button = st.button("Ckeck")


with st.spinner("Discovering Answers.."):
    # used try catch because not neccery to show errors in gui
    if button:
        prediction(news)
