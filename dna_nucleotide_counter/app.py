# importing
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# # page title
# image = Image.open("image2.jpg")
# st.image(image)

st.write("""
# Bio Informatics Web App

This will counts the nucleotide composition of query DNA!
***
""")

st.header("Enter DNA sequence")
input = "tatcttatctatacagcaaaacggaccccgaaagcttgcccgtcccatctacattggtgtatatttaagaaagtcagtactcagcacgcatccttgtactc"
# adding textbox
seq = st.text_area("Enter Sequence here", input, height=25)
seq = seq.upper()
seq = seq.splitlines()

seq = "".join(seq)

st.write("""***""")
st.header("Input DNA Query")
st.write(seq)

# print


def DNA_count(seq):
    d = dict([("A", seq.count("A")), ("T", seq.count("T")),
             ("G", seq.count("G")), ("C", seq.count("C"))])

    return d


X = DNA_count(seq)
st.subheader("print dictonary")
# X

X_labels = list(X)
X_values = list(X.values())

st.subheader("output")
st.write("A ", str(X["A"]))
st.write("T ", str(X["T"]))
st.write("G ", str(X["G"]))
st.write("C ", str(X["C"]))


# dataframe
st.subheader("Dataframe")
df = pd.DataFrame.from_dict(X, orient="index")
df = df.rename({0: "count"}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns={"index": "nucleotide"})
st.write(df)

# print bar chart
st.subheader("Bar chart")
p = alt.Chart(df).mark_bar().encode(
    x="nucleotide",
    y="count"
)
# adjuesting the bar chart
p = p.properties(width=alt.Step(80))
st.write(p)
