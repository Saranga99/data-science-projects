import streamlit as st
from pdfminer.high_level import extract_text
import os
import re
import textract

# save uploaed file as tempory


def save_uploadedfile(uploadedfile):
    with open(os.path.join("temp", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("File:{} Successfully Saved".format(uploadedfile.name))

# write to tempory text file


def write_to_txt(text):
    st.write(text)
    lines = [text]
    with open('temp/tempory.txt', 'w') as f:
        for line in lines:
            f.write(line)
            f.write('')
    st.info("File Saved Successfully (txt)")

# clean text


def clean_text(text):
    # Convert to string
    # text = text.decode('utf-8')
    # Replace "\r\n" with spaces
    text = text.replace("\r\n", " ")
    # Remove any double spaces
    text = re.sub(" +", " ", text)
    # removing new line characters
    text = re.sub('\n ', '', str(text))
    text = re.sub('\n', ' ', str(text))
    # removing apostrophes
    text = re.sub("'s", '', str(text))
    # removing hyphens
    text = re.sub("-", ' ', str(text))
    text = re.sub("— ", '', str(text))
    # removing quotation marks
    text = re.sub('\"', '', str(text))
    # removing any reference to outside text
    text = re.sub("[\(\[].*?[\)\]]", "", str(text))
    return text


# email - regular expression
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')


# extract all emails in input text
def get_emails(text):
    return re.findall(EMAIL_REG, text)


#header and description
st.title("Invoice Information Extractor")
st.write("This Application will extract information from Invoices in .pdf format")
# file upload
uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

if uploaded_file is not None:
    file_details = {"FileName": uploaded_file.name,
                    "FileType": uploaded_file.type}
#    df  = pd.read_csv(datafile)
#    st.dataframe(df)
    save_uploadedfile(uploaded_file)

extract = st.button("Extract Information")
# method for save to .txt button if file uploaded and saved informaation will be shown
if extract and uploaded_file is not None:
    # extract type 1
    text = extract_text("temp/" + uploaded_file.name)
    # extract type 2
    #text = textract.process("temp/" + uploaded_file.name)
    st.subheader("text")
    st.write(text)
    cleaned_text = clean_text(text)
    st.subheader("cleaned")
    st.write(cleaned_text)
    if len(get_emails(cleaned_text)) > 0:
        st.write("Email          : ", get_emails(cleaned_text)[0])
    os.remove("temp/" + uploaded_file.name)
