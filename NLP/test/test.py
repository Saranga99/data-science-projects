# D:\iit\CV\Saranga Kumarapeli.pdf
import re
import nltk
import docx2txt
# import pdftotext
from pdfminer.high_level import extract_text

text = ""


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


while True:
    try:
        path = input("Enter Your path Here : ")
        print(extract_text_from_pdf(path))
        break
    except:
        print("Please Enter Correct Path")
print(text)
