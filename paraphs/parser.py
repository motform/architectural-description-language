"""
4ME501 - Programming for Digital Humanities - 2018
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Modulse does two things
"""

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
import sys


def read_input(file):
    """Open UTF-8 file and return complete contents as string."""
    try:
        with open(file, 'rt', encoding='UTF-8') as file:
            return file.read()
    except UnicodeDecodeError:
        print("Unable to decode file, pass a file with valid UTF-8 encoding.")
        sys.exit(1)


def remove_stop_words(text):
    """Cleans a text from stopwords with set provided from the NLTK.
    Note that this need to be manually downloaded. See Readme."""
    stop_words = set(stopwords.words('english'))
    text = word_tokenize(text)
    text = [word for word in text if word not in stop_words]
    return ' '.join(text)


def generate_tags(text):
    """Parses a text using Textblob and returns a generator."""
    tags = TextBlob(text).tags
    for word, tag in tags:
        yield word, tag


def generate_sentiment(text, type_of_sentiment: str):
    """Parses a text using textblob and returnes the semtiment (polarity) value"""
    if type_of_sentiment == 'subjectivity':
        return TextBlob(text).sentiment.subjectivity
    elif type_of_sentiment == 'polarity':
        return TextBlob(text).sentiment.polarity
    else:
        print('You need to specify what type of sentiment to generate.')
        sys.exit(-10)

