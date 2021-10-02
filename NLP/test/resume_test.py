
# D:\iit\CV\Saranga Kumarapeli.pdf
import re
import nltk
import docx2txt
# import pdftotext
from pdfminer.high_level import extract_text


path = input("Enter Your path Here : ")


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


if __name__ == '__main__':
    print(extract_text_from_pdf(path))


# extract names
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None


def extract_names(txt):
    person_names = []

    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                person_names.append(
                    ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
                )

    return person_names


if __name__ == '__main__':
    text = extract_text_from_docx('Saranga Kumarapeli.docx')
    names = extract_names(text)

    if names:
        print(names)


# email
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


def extract_emails(resume_text):
    return re.findall(EMAIL_REG, resume_text)


if __name__ == '__main__':
    text = extract_text_from_pdf(path)
    emails = extract_emails(text)

    if emails:
        print(emails)
