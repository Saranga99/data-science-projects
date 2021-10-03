# D:\iit\CV\Saranga Kumarapeli.pdf
from pdfminer.high_level import extract_text
import nltk
import re
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# import pdftotext
print("\n_____Resume Information Extractor - CLI based Application_____\n")


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


while True:
    try:
        path = input("Enter Your path Here : ")
        lines = [extract_text_from_pdf(path)]
        with open('readme.txt', 'w') as f:
            for line in lines:
                f.write(line)
                # f.write('')
        break
    except:
        print("\nPlease Enter Correct Path\n")

with open("readme.txt", "r") as myfile:
    data = myfile.read()


def extract_names(txt):
    person_names = []

    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                person_names.append(
                    ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
                )

    return person_names


names = extract_names(data)
if names:
    print("\n____Extracted Information____\n")

    print("Name           : ", names[3][:-8])

# email
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')


def extract_emails(resume_text):
    return re.findall(EMAIL_REG, resume_text)


emails = extract_emails(data)
if emails:
    print("Email          : ", emails[0])


# phone = []
# for i in re.findall(r'\+[-()\s\d]+?(?=\s*[+<])', data):
#     phone.add(i)

# # print(data)
# print(type(data))

# mobile number
phone = []
for i in re.findall(r'(\s+([0-9]+\s+)+)', data):
    phone.append(i)

print("Telephone No.  :", phone[1][0], "/", phone[2][0])
