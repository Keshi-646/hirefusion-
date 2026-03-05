import pdfplumber
import re


KNOWN_SKILLS = [
    "python","java","c++","sql","excel","machine learning","deep learning",
    "pandas","numpy","statistics","data analysis","tensorflow","pytorch",
    "scikit-learn","flask","django","html","css","javascript"
]


def extract_text(file):

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            t = page.extract_text()

            if t:
                text += t + " "

    return text.lower()


def extract_name(text):

    lines = text.split("\n")

    for line in lines[:10]:

        if len(line.split()) <= 4:
            return line.strip()

    return "Unknown"


def extract_skills(text):

    found = []

    for skill in KNOWN_SKILLS:

        if skill in text:
            found.append(skill)

    return list(set(found))