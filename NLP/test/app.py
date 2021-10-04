# importings
from transformers import pipeline
import streamlit as st
from PIL import Image
from pdfminer.high_level import extract_text
import nltk
import re

#header and description
st.header("Resume Information Extractor")
st.write("This Application will extract information from Resumes in .pdf format")
# file upload
uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
# button to save uploaded .pdf text into .txt file
btnSave = st.button("Save to .txt")
image = Image.open("github.png")


# name extraction method


def extract_names(txt):
    # this list contains extracted names
    person_names = []

    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                person_names.append(
                    ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
                )
    return person_names


# email extraction method and regular expression for mails
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')


def extract_emails(resume_text):
    # find all the matched text with regular expression
    return re.findall(EMAIL_REG, resume_text)

# mobileno extraction method


def extract_numbers(resume_text):
    phone = []
    for i in re.findall(r'(\s+([0-9]+\s+)+)', resume_text):
        # trying to add only numbers legnth larger than 9, mobile no>=9
        for j in i:
            if len(j) > 9:
                phone.append(j)
    return phone


# method for save to .txt button if file uploaded and saved informaation will be shown
if btnSave:
    if uploaded_file is not None:
        text = extract_text(uploaded_file)
        lines = [text]
        with open('streamlit.txt', 'w') as f:
            for line in lines:
                f.write(line)
                # f.write('')
        st.info("File Saved Successfully")

# if .pdf file is uploaded extract relevant information and will be shown in proper format
if uploaded_file is not None:
    st.info("File Uploaded Successfully")
    # st.write(extract_text(uploaded_file))
    text = extract_text(uploaded_file)
    st.subheader("Extracted Textual Data")
    # shown extracted relavant data on the page
    st.write("\nNames", extract_names(text), "\nEmails",
             extract_emails(text), "\nNumbers", extract_numbers(text))
    names, emails, numbers = extract_names(
        text), extract_emails(text), extract_numbers(text)
    st.subheader("Extracted Textual Information")
    # filtering relavant information from extracted data
    st.write("Name: ", names[3][:-8])
    st.write("Email: ", emails[0])
    st.write("Telephone No.:", numbers[0], "/", numbers[2])
else:
    # if file is not uploaded this will be shown
    st.error("No file uploaded")


# git hub logo and repo link
st.write("\n")
st.image(image)
st.write(
    " [Git Hub](https://github.com/Saranga99/data-science-projects/tree/main/NLP)")


@st.cache(allow_output_mutation=True)
def load_qa_model():
    model = pipeline("question-answering")
    return model


qa = load_qa_model()
st.title("Ask Questions about your Text")
sentence = st.text_area('Please paste your article :', height=30)
question = st.text_input("Questions from this article?")
button = st.button("Get me Answers")
max = st.sidebar.slider('Select max', 50, 500, step=10, value=150)
min = st.sidebar.slider('Select min', 10, 450, step=10, value=50)
do_sample = st.sidebar.checkbox("Do sample", value=False)
with st.spinner("Discovering Answers.."):
    if button and sentence:
        answers = qa(question=question, context=sentence)
        st.write(answers['answer'])
