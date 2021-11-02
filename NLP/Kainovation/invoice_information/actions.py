import re


class Actions(object):
    # clean text
    def clean_text(text):
        # Convert to string
        text = text.decode('utf-8')
        # Replace "\r\n" with spaces
        text = text.replace("\r\n", "")
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
        return text

    # extract all emails in input text

    def get_emails(text):
        # email - regular expression
        EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
        return re.findall(EMAIL_REG, text)
