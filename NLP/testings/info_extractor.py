# importings
from transformers import pipeline
from pdfminer.high_level import extract_text
import nltk
import re

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# import pdftotext
print("\n_____Resume Information Extractor - CLI based Application_____\n")

# extract all textual infomation in high_level


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


def load_qa_model():
    model = pipeline("question-answering")
    return model


# extract all names in input text and return as a list
def extract_names(txt):
    person_names = []

    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                person_names.append(
                    ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
                )

    return person_names


# email - regular expression
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')


# extract all emails in input text
def extract_emails(resume_text):
    return re.findall(EMAIL_REG, resume_text)


# mobile number
def extract_mobile_numbers(resume_text):
    phone = []
    for i in re.findall(r'(\s+([0-9]+\s+)+)', resume_text):
        phone.append(i)
    return phone


# it took some time to load model on my lap :D so i put this for inform it to user
print("Please wait buddy... I'm Loading..... :D")
qa = load_qa_model()

# main loop fot the application
while True:
    user_input = input(
        "Press any key to add resume path, press 'q' to Exit from the Application : ")
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
                # eg :- Saranga Kumarapeli.pdf
                path = input("Enter Your path Here : ")
                lines = [extract_text_from_pdf(path)]
                with open('readme.txt', 'w') as f:
                    for line in lines:
                        f.write(line)
                        # f.write('')
                break
            except:
                print("\nPlease Enter Correct Path\n")

        # open written text file and load in a variable
        with open("readme.txt", "r") as myfile:
            data = myfile.read()

        # calling methods
        names = extract_names(data)
        if names:
            print("\n____Extracted Information____\n")

            print("Name           : ", names[3][:-8])

        emails = extract_emails(data)
        if emails:
            print("Email          : ", emails[0])

        numbers = extract_mobile_numbers(data)
        print("Telephone No.  :", numbers[1][0], "/", numbers[2][0])

        # QA module loop, user can ask any nuber of questons until bored
        while True:
            user_input = input(
                "\nPress 'y' to ask question from cv, press 'q' Proceed without asking Questions : ")
            user_input = user_input.lower()
            if user_input == "y":
                question = input("\nAsk Your Question : ")
                try:
                    answers = qa(question=question, context=data)
                    print("\nAnswer : ", answers['answer'],
                          "\n", "Score : ", answers["score"])
                # sometimes model couldnt predict the answer, that's how here we say that :D
                except:
                    print("\nsorry..I Couldn't find any answer :D")
            # if this true app will go to main loop
            elif user_input == "q":
                print("\nThank you for using, Stay safe !!!")
                break
            else:
                print("\nPlease Enter Correct inputs to proceed :D")
