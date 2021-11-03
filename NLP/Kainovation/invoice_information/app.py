import streamlit as st
# from pdfminer.high_level import extract_text
import os
# import textract
from actions import Actions
import fitz
from actions import EXTRACTOR


# header and description
st.title("Invoice Information Extractor")
st.write("This Application will extract information from Invoices in .pdf format")
# file upload
uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

if uploaded_file is not None:
    file_details = {"FileName": uploaded_file.name,
                    "FileType": uploaded_file.type}
    Actions.save_uploadedfile(uploaded_file)

extract = st.button("Extract Information")
# method for save to .txt button if file uploaded and saved informaation will be shown
if extract and uploaded_file is not None:
    # extract type 1
    # text = extract_text("temp/" + uploaded_file.name)
    # extract type 2
    # text = textract.process("temp/" + uploaded_file.name)

    # pymu pdf codes
    path = "temp/"+uploaded_file.name
    text = EXTRACTOR.extract_text(path)

    st.subheader("text")
    st.write(text)
    cleaned_text = Actions.clean_text(text)
    st.subheader("cleaned")
    st.write(cleaned_text)
    emails = Actions.get_emails(cleaned_text)
    if len(emails) > 0:
        st.write("Email          : ", emails[0])
    st.write("Mobile Numbers : ", Actions.get_mobile_numbers(cleaned_text))
    st.write("Invoice Amount : ", Actions.get_invoice_amount(cleaned_text))
    st.write(Actions.get_dates(cleaned_text))

    os.remove("temp/" + uploaded_file.name)
