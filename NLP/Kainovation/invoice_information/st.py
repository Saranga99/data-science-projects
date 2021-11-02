import streamlit as st
from pdfminer.high_level import extract_text
import os
import re
import textract
from actions import Actions
# import fitz

# save uploaed file as tempory


def save_uploadedfile(uploadedfile):
    with open(os.path.join("temp", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("File:{} Successfully Saved".format(uploadedfile.name))

# write to tempory text file


def write_to_txt(file):
    for pagenumber, page in enumerate(file.pages(), start=1):
        text = page.getText()
        txt = open(f"invoice_page_{pagenumber}.txt", "a")
        txt.writelines(text)
        txt.close()


#header and description
st.title("Invoice Information Extractor")
st.write("This Application will extract information from Invoices in .pdf format")
# file upload
uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

if uploaded_file is not None:
    file_details = {"FileName": uploaded_file.name,
                    "FileType": uploaded_file.type}
    save_uploadedfile(uploaded_file)

extract = st.button("Extract Information")
# method for save to .txt button if file uploaded and saved informaation will be shown
if extract and uploaded_file is not None:
    actions = Actions()
    # extract type 1
    # text = extract_text("temp/" + uploaded_file.name)
    # extract type 2
    text = textract.process("temp/" + uploaded_file.name)

    # pymu pdf codes
    # file = fitz.open("temp/" + uploaded_file.name)
    # text = write_to_txt(file)
    st.subheader("text")
    st.write(text)
    cleaned_text = clean_text(text)
    st.subheader("cleaned")
    st.write(cleaned_text)
    emails = Actions.get_emails(cleaned_text)
    if len(emails) > 0:
        st.write("Email          : ", emails[0])
    os.remove("temp/" + uploaded_file.name)
