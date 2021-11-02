# importings
from pdfminer.high_level import extract_text
# import nltk
# import re

import os
import spacy
import re
from dateutil.parser import *
import textract

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# import pdftotext
print("\n_____Resume Information Extractor - CLI based Application_____\n")

# extract all textual infomation in high_level


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


# main loop fot the application
while True:
    user_input = input(
        "\nPress any key to add resume path, press 'q' to Exit from the Application : ")
    # converting user input to the lowercase
    user_input = user_input.lower()
    if user_input == "q":
        print("\nThank you for using, Stay safe !!!")
        break
    else:
        # sub loop for get exact correct path from user, this will break when user enters a correct path
        while True:
            # try and try one day you will find the path :D
            try:
                path = input("\nEnter Your path Here : ")
                lines = [extract_text_from_pdf(path)]
                with open('resume_text.txt', 'w') as f:
                    for line in lines:
                        f.write(line)
                        # f.write('')
                content = extract_text_from_pdf(path)
                content = " ".join(content.replace(
                    u"\xa0", " ").strip().split())
                print(content)
                break
            except:
                print("\nPlease Enter Correct Path\n")
