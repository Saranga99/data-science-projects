import streamlit as st
import pandas as pd

with st.sidebar:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-oEZwKkXIlxSefwhTTwuUyaH8lCwtRyy8eO49DIpZthel7j8eZYxeQOg6iKxBIBnlASg&usqp=CAU")
    st.title("AutoML")
    selection=st.radio("ML Flow",["Upload","Profiling","ML","Download"])
    st.info("This application automate your Supervised Learing Tasks using Streamlit, Pandas Profiling and PyCaret")
    # st.radio()

if selection=="Upload":
    st.title("Upload your Data")
    data=st.file_uploader("Upload here")
    if data:
        df=pd.read_csv(data)
        st.dataframe(df)

if selection=="Profiling":
    pass

if selection=="ML":
    pass

if selection=="Download":
    pass
