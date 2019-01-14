"""
4ME501 - Programming for Digital Humanities - 2018
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Text parsing using TextBlob.
"""

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
import ntpath
import sys


def read_file(file):
    """Open UTF-8 file and return complete contents as string."""
    try:
        with open(file, 'rt', encoding='UTF-8') as file:
            return file.read()
    except UnicodeDecodeError:
        print("Unable to decode file, pass a file with valid UTF-8 encoding.")
        sys.exit(1)


def get_filename(file, file_extension='.svg'):
    """Reads name of an input file and converts it into a suitable output name."""
    file = ntpath.basename(file)
    file = file.split('.')[0]
    return file + file_extension


def remove_stop_words(text):
    """Cleans a text from stopwords.
    Stop word set provided from the NLTK."""
    stop_words = set(stopwords.words('english'))
    text = word_tokenize(text)
    text = [word for word in text if word not in stop_words]
    return ' '.join(text)


def generate_tags(text):
    """Parses a text using Textblob and returns a
    generator object."""
    tags = TextBlob(text).tags
    for word, tag in tags:
        yield word, tag


def generate_sentiment_polarity(text):
    """Parses a text using textblob and returnes the semtiment (polarity) value"""
    return TextBlob(text).sentiment.polarity


def generate_sentiment_subjectivity(text):
    """Parses a text using textblob and returnes the semtiment (polarity) value"""
    return TextBlob(text).sentiment.subjectivity
