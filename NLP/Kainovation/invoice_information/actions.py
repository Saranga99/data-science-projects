import re
import streamlit as st
import os


class Actions(object):
    # save uploaed file as tempory
    def save_uploadedfile(uploadedfile):
        with open(os.path.join("temp", uploadedfile.name), "wb") as f:
            f.write(uploadedfile.getbuffer())
        return st.success("File:{} Successfully Saved".format(uploadedfile.name))

    # clean text
    def clean_text(text):
        # Convert to string
        text = text.decode('utf-8')
        # Replace "\r\n" with spaces
        text = text.replace("\r\n", ",")
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

    # extract all emails in input text
    def get_emails(text):
        # email - regular expression
        EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
        return re.findall(EMAIL_REG, text)

    # write to tempory text file
    def write_to_txt(file):
        for pagenumber, page in enumerate(file.pages(), start=1):
            text = page.getText()
            txt = open(f"invoice_page_{pagenumber}.txt", "a")
            txt.writelines(text)
            txt.close()

    # mobile number
    def get_mobile_numbers(text):
        phone = []
        for i in re.findall(r"\(\d{2,4}\)\d{6,7}", text):
            phone.append(i)
        for i in re.findall(r"\d{3}-\d{8}|\d{4}-\d{7}", text):
            phone.append(i)
        for i in re.findall(r"^.*\s([\d\s]{11,14})\s.*$", text):
            phone.append(i)
        return phone
