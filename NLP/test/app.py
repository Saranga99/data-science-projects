# importings
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


# image
st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="data:image/png;base64,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" />
    </a>''',
            unsafe_allow_html=True
            )
