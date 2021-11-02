import streamlit as st
from transformers import pipeline
from pdfminer.high_level import extract_text

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")


@st.cache(allow_output_mutation=True)
def load_qa_model():
    model = pipeline("question-answering")
    return model


qa = load_qa_model()

st.header("Ask Questions")
question = st.text_input("Questions from this CV?")
# button
button = st.button("Get me Answers")

if uploaded_file is not None:
    # getting data
    text = extract_text(uploaded_file)
    # waitng time to find answe, inform it to user
    with st.spinner("Discovering Answers.."):
        # used try catch because not neccery to show errors in gui
        if button and uploaded_file:
            try:
                # try to get answers form cv extracted data
                answers = qa(question=question,
                             context=text)
                st.write(answers['answer'])
            except:
                st.info("Sorry..I Couldn't find any answer :D")
