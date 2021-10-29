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


text = extract_text("3.pdf")
print(clean_Text(text), is_Invoice_Or_not(text))
