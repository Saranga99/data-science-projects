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

#streamlit section
department=df["Department"].unique().tolist()
ages=df["Age"].unique().tolist()


age_section=st.slider("Age:",
                    min_value=min(ages),
                    max_value=max(ages),
                    value=(min(ages),max(ages)))

depaertment_selection=st.multiselect("Department:",
                                    department,
                                    default=department)


#data filtering
mask=(df["Age"].between(*age_section)) & (df["Department"].isin(depaertment_selection))

number_of_result=df[mask].shape[0]
st.markdown(f"*Available Results:*{number_of_result}")



#group dataframe
df_grouped=df[mask].groupby(by=["Rating"]).count()[["Age"]]
df_grouped=df_grouped.rename(columns={"Age":"Votes"})
df_grouped=df_grouped.reset_index()


##plotting bar
bar_chart=px.bar(df_grouped,
                x="Rating",  
                y="Votes",
                text="Votes",
                template="plotly_white")

#inserting bar chart
st.plotly_chart(bar_chart)



#pie chart
pie_chart=px.pie(df_participant,
                title="Total No. of Participants",
                values="Participants",
                names="Departments")

#inserting ploty chart
st.plotly_chart(pie_chart)











