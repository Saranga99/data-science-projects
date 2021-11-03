import streamlit as st
import os
from actions import Actions


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
    # pymu pdf codes
    path = "temp/"+uploaded_file.name
    text = Actions.extract_text(path)

    save_image_path = 'temp/'+uploaded_file.name
    with open(save_image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    col1, col2 = st.columns(2)
    col1.header("Invoice Uploaded")
    Actions.show_pdf(path)

    # st.subheader("text")
    # st.write(text)
    cleaned_text = Actions.clean_text(text)
    # st.subheader("cleaned")
    # st.write(cleaned_text)

    emails = Actions.get_emails(cleaned_text)
    if len(emails) > 0:
        st.write("Email          : ", emails[0])
    st.write("Mobile Numbers : ", Actions.get_mobile_numbers(cleaned_text))
    st.write("Invoice Amount : ", Actions.get_invoice_amount(cleaned_text))
    st.write(Actions.get_dates(cleaned_text))

    os.remove("temp/" + uploaded_file.name)
