import pickle
import streamlit as st


#header and description
st.title("Fake News Classifier")
st.write("This Application will Classify news into fake or true")
# loading the trained model
pickle_in = open('log_reg.pkl', 'rb')
classifier = pickle.load(pickle_in)


@st.cache()
