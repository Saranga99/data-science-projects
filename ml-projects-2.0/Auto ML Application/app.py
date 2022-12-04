import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import os
#ML
from pycaret.regression import setup, compare_models, save_model
from pycaret.classification import setup, compare_models, save_model


with st.sidebar:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-oEZwKkXIlxSefwhTTwuUyaH8lCwtRyy8eO49DIpZthel7j8eZYxeQOg6iKxBIBnlASg&usqp=CAU")
    st.title("AutoML")
    selection=st.radio("ML Flow",["Upload","Profiling","ML","Download"])
    st.info("This application automate your Supervised Learing Tasks using Streamlit, Pandas Profiling and PyCaret")
    # st.radio()

if os.path.exists("source_data.csv"):
    df=pd.read_csv("source_data.csv",index_col=None)

if selection=="Upload":
    st.title("Upload your Data")
    data=st.file_uploader("Upload here")
    if data:
        df=pd.read_csv(data,index_col=None)
        df.to_csv("source_data.csv",index=None)
        st.dataframe(df)

if selection=="Profiling":
    st.title("Exploratory Data Analysis")
    profile_report=df.profile_report()
    st_profile_report(profile_report)


if selection=="ML":
    st.title("Machine Learning Modeling")
    ml_type=st.selectbox("Select your Problem type",["Regression","Classification"])

if selection=="Download":
    pass
