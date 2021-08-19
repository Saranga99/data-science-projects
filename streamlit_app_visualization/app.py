import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

image=Image.open("images\img.jpg")


st.set_page_config(page_title="Survay Results")
st.header("Results 2021")
st.subheader("Results for the year 2021")

#add image
st.image(image,caption="data_visualization",use_column_width=True)

#data
excel_file="data.xlsx"
sheet_name="DATA"
df = pd.read_excel(excel_file, sheet_name=sheet_name,usecols="B:D",header=3)
df_participant = pd.read_excel(excel_file, sheet_name=sheet_name,usecols="F:G",header=3)
st.dataframe(df)


df_participant.dropna(inplace=True)
#pie chart
pie_chart=px.pie(df_participant,
                title="Total No. of Participants",
                values="Participants",
                names="Departments")

#inserting ploty chart
st.plotly_chart(pie_chart)







