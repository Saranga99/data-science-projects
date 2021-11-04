import re
import streamlit as st
import os
import datefinder
import fitz
import base64

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


class Actions(object):
    # save uploaed file as tempory
    def save_uploadedfile(uploadedfile):
        with open(os.path.join("temp", uploadedfile.name), "wb") as f:
            f.write(uploadedfile.getbuffer())
        return st.success("File:{} Successfully Saved".format(uploadedfile.name))

    # clean text
    def clean_text(text):
        text = text.lower()
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
        text = text.replace("�", " \n")
        text = text.replace(":", " ")
        return text

    # extract all emails in input text
    def get_emails(text):
        # email - regular expression
        EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
        return re.findall(EMAIL_REG, text)

    # write to tempory text file
    def write_to_txt(text):
        lines = [text]
        with open('temp/temp_txt.txt', 'w') as f:
            for line in lines:
                f.write(line)
                # f.write('')

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

    # get dates
    def get_dates(text):
        start_index = text.find("invoice date")
        end_index = start_index + len("invoice date")+30
        date = text[start_index:end_index]
        date = list(datefinder.find_dates(date))
        return date

    # extract text

    def extract_text(path):
        doc = fitz.open(path)
        text = ""
        for i in range(doc.pageCount):
            page = doc.load_page(i)
            pagetext = page.get_text()
            text += pagetext
        return text

    # pdf show in interface
    def show_pdf(file_path):
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)

    # getinvoice amount
    def get_invoice_number(text):
        text = text.lower()
        # st.write(text)
        # for txt in text:
        #     if txt == "invoice no" or txt == "invoice number":
        #         text = "yes"
        #     else:
        #         text = "no"
        # valid_invoice_tags = ['invoice', 'lading',
        #                       'bill no', "invoice number", "ao invoice no.", "tax", "items"]
        # output = [i for i in text if i in valid_invoice_tags]
        # if len(output) > 0:
        #     return "invoice"
        # else:
        #     return "not"

        matches = re.findall(
            r'(?<=\binvoice )(?:.*?)(?= invoice\b)', text, flags=re.DOTALL)
        for i, match in enumerate(matches):
            # match=(f'\nMatch {i + 1}:\n', match, sep='')
            match = match.split(" ")
        #print(f'\nMatch {i + 1}:\n', match, sep='')
            for i in match:
                if len(i) == 10 and i.isdecimal():
                    no = i

        return no
