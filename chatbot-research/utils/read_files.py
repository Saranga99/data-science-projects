import docx2txt

def read_docx(filename):
    text = docx2txt.process(filename)
    # print(text)
    return text