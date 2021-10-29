# some python file
# import textract
# text = textract.process("1.pdf")

from pdfminer.high_level import extract_text
import re


def clean_Text(text):

    # Convert to string
    # text = text.decode('utf-8')

    # Replace "\r\n" with spaces
    text = text.replace("\r\n", " ")

    # Remove any double spaces
    text = re.sub(" +", " ", text)

    return text


def is_Invoice_Or_not(text):

    tokens = text.lower().split()

    valid_invoice_tags = ['invoice', 'lading', 'bill']

    output = [i for i in tokens if i in valid_invoice_tags]

    if len(output) > 0:
        return "Invoice"
    else:
        return "Not an Invoice"


def Get_Tag_Position(tag, text, direction='forward'):

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


def Parse_Amounts(text):

    money = re.compile('|'.join([
        r"\$?\d+\.?\d+\,\d{1,2} ",  # EUR format
        r"\$?\d+\,?\d+\.\d{1,2} ",  # USD format
        r"\$\d+\,?\d*\.?\d{1,2} ",  # USD format without decimals
    ]))

    matches = re.findall(money, text)

    matches = [i.strip() for i in matches]

    return matches


text = extract_text("3.pdf")
print(clean_Text(text), is_Invoice_Or_not(text))
