import re

def clean_text(text):
    text = str(text)

    # lowercase
    text = text.lower()

    # remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # remove mentions
    text = re.sub(r"@\w+", "", text)

    # remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text