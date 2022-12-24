import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import os
import h2o
from h2o.automl import H2OAutoML
# Start the H2O cluster (locally)
h2o.init()
#ML
# from pycaret.regression import setup, compare_models,pull, save_model
from pycaret.classification import *


with st.sidebar:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-oEZwKkXIlxSefwhTTwuUyaH8lCwtRyy8eO49DIpZthel7j8eZYxeQOg6iKxBIBnlASg&usqp=CAU")
    st.title("AutoML")
    selection=st.radio("ML Flow",["Upload","Profiling","ML","Download"])
    st.info("This application automate your Supervised Learing Tasks using Streamlit, Pandas Profiling and PyCaret")
    # st.radio()

if os.path.exists("source_data.csv"):
    df=pd.read_csv("source_data.csv")

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
    chosen_target=st.selectbox("Select Your Target",df.columns)
    if st.button('Run Modelling'):
        if ml_type=="Regression":
            pass
        
        if ml_type=="Classification":
            # setup(df, target = chosen_target, preprocess=True)
            # setup_df = pull()
            # st.dataframe(setup_df)
            # best_model = compare_models()
            # compare_df = pull()
            # st.dataframe(compare_df)
            # save_model(best_model, 'best_model')
            pass




if selection=="Download":
    pass
