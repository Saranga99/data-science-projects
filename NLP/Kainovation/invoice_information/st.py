import streamlit as st
from pdfminer.high_level import extract_text
import os

# save uploaed file as tempory


def save_uploadedfile(uploadedfile):
    with open(os.path.join("temp", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved File:{} to tempDir".format(uploadedfile.name))


#header and description
st.title("Invoice Information Extractor")
st.write("This Application will extract information from Invoices in .pdf format")
# file upload
uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
# button to save uploaded .pdf text into .txt file


if uploaded_file is not None:
    file_details = {"FileName": uploaded_file.name,
                    "FileType": uploaded_file.type}
#    df  = pd.read_csv(datafile)
#    st.dataframe(df)
    save_uploadedfile(uploaded_file)

extract = st.button("Extract Information")
# method for save to .txt button if file uploaded and saved informaation will be shown
if extract:
    if uploaded_file is not None:
        text = extract_text("../temp/" + uploaded_file.name)
        st.write(text)
        lines = [text]
        with open('resume _text_st.txt', 'w') as f:
            for line in lines:
                f.write(line)
                # f.write('')
        st.info("File Saved Successfully")
