

# import pip
# pip.main(["install","streamlit"])
import streamlit as st
from PIL import Image
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score



df=pd.read_csv("diabetes.csv")
df.head()
st.header("Diabetes Detection Application")
st.write("Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy.")
image=Image.open("diabetes.jpg")


st.image(image)
st.write("")
st.subheader("Dataset")
st.dataframe(df)

st.subheader("Descriptive")
st.write(df.describe())















