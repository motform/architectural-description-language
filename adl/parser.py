"""
4ME501 - Programming for Digital Humanities - 2018
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Text parsing using TextBlob.
"""

from textblob import TextBlob


def generate_tags(text):
    """
    Parses a text using Textblob and returns a
    generator object.
    """
    tags = TextBlob(text).tags
    for word, tag in tags:
        yield word, tag


def generate_sentiment(text):
    """Parses a text using textblob and returnes the semtiment (polarity) value"""
    return TextBlob(text).sentiment.polarity
