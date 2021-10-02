# D:\iit\CV\Saranga Kumarapeli.pdf
import re
import nltk
import docx2txt
# import pdftotext
from pdfminer.high_level import extract_text
print("\nResume Information Extractor - CLI based Application\n")


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


while True:
    try:
        path = input("Enter Your path Here : ")
        print(extract_text_from_pdf(path))
        lines = [extract_text_from_pdf(path)]
        with open('readme.txt', 'w') as f:
            for line in lines:
                f.write(line)
                # f.write('')
        break
    except:
        print("\nPlease Enter Correct Path\n")

with open("readme.txt", "r") as myfile:
    data = myfile.read().splitlines()
print(data)
print(type(data[0]))
