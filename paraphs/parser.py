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
