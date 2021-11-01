from datetime import datetime
import pandas as pd
import streamlit as st
import re
import textract
import datefinder

# validate uploaded file is invoice or not:


def is_invoice_Or_not(text):
    tokens = text.lower().split()
    # tags to filter invoices from other docs
    valid_invoice_tags = ['invoice', 'lading',
                          'bill', "invoice number", "invoice no", "tax", "items"]
    output = [i for i in tokens if i in valid_invoice_tags]
    if len(output) > 0:
        return "invoice"
    else:
        return "not"

# get the tag position


def get_tag_position(tag, text, direction='forward'):
    tag = tag.lower()
    if direction == 'reverse':
        tag_pos = text.lower().rfind(tag)
    else:
        tag_pos = text.lower().find(tag)
    if tag_pos > 0:
        start_pos = tag_pos + len(tag) + 1
    else:
        start_pos = -1
    return start_pos

# phrase amount


def parse_amounts(text):

    money = re.compile('|'.join([
        r"\$?\d+\,?\d+\.\d{1,2} ",  # USD format
        r"\$\d+\,?\d*\.?\d{1,2} ",  # USD format without decimals

    ]))
    matches = re.findall(money, text)
    matches = [i.strip() for i in matches]
    return matches

# getinvoice amount


def get_invoice_amount(text):
    text = text.lower()
    invoice_amount = ""
    amounts = parse_amounts(text)
    if len(amounts) > 0:
        invoice_amount = amounts[-1]
    else:
        temp_corpus = text[get_tag_position(
            "total", text, direction='reverse'):]
        numbers = re.findall("\d+", temp_corpus)
        if len(numbers) > 0:
            invoice_amount = numbers[0]
    return invoice_amount


# clean text:


def clean_text(text):
    # Convert to string
    text = text.decode('utf-8')
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


# mobile number
def get_mobile_numbers(text):
    phone = []
    for i in re.findall(r"\(\d{2,4}\)\d{6,7}", text):
        phone.append(i)
    for i in re.findall(r"\d{3}-\d{8}|\d{4}-\d{7}", text):
        phone.append(i)
    return phone


# header and description:
st.title("Invoice Information Extractor")
st.write("This Application will extract information from Invoices in .pdf format")
# file upload
#uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

# C:\Users\Saranga\Desktop\data-science-projects\NLP\Kainovation\invoice_information\1.pdf
# C:/Users/Saranga/Desktop/data-science-projects/NLP/Kainovation/invoice_information/1.pdf
path = st.text_input('Input your file path')
extract = st.button("extract")
if path is not None and extract:
    try:
        text = textract.process(path)
        cleaned_text = clean_text(text)
        type = is_invoice_Or_not(cleaned_text)
        if type == "invoice":
            st.subheader("Cleaned Text from Invoice\n")
            st.write(cleaned_text, "\n")
            st.write("Invoice Number : ",)
            st.write("Email          : ", get_emails(cleaned_text)[0])
            st.write("Mobile Numbers : ", get_mobile_numbers(cleaned_text))
            st.write("Invoice Amount : ", get_invoice_amount(cleaned_text))

            matches = list(datefinder.find_dates(cleaned_text))
            if len(matches) > 0:
                # date returned will be a datetime.datetime object. here we are only using the first match.
                date = matches[0]
                st.write("Date      : ", date)
            else:
                st.write('No dates found')

        else:
            st.error("your file is't an invoice")
    except:
        # if file is not exist this will be shown
        st.error("No such a file at the location")
