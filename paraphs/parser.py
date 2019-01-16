"""
4ME501 - Programming for Digital Humanities - 2018
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Modulse does two things
"""
from zlib import crc32
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
from random import Random
import sys


class Token(object):
    """Token object - container for textblob-tokens.
    Encapsulates the tokenized word, its tag and the
    numeric representations used by the stencils.

    Includes the following:
    Word    - the tokenized word
    Tag     - the Penn Treebank POS tag
    Value   - the word represented as a float
    Random  - an instance of a random object. We want the random values to be
              deterministic for every occurance of the same word, so we use
              the rand on an object rather than module level.
    uniform - sugar for token.random.uniform"""

    def __init__(self, word, tag):
        self.word = word
        self.tag = tag
        self.value = self.str_to_float(self.word)
        self.random = Random(self.value)
        self.uniform = self.random.uniform

    def str_to_float(self, word, encoding="utf-8"):
        """The Cairo context is normalised to a [0:1] scale.
        This helps out with the drawing functions, but makes hash()
        inadaquite, as it only outputs integers. Instead, we use a crc32
        function to make normalised and unsigned floats in our range.

        The Python std:lib implementation of crc32 requires bytestrings,
        which is why we include an explicit conversion step.

        Credit to https://stackoverflow.com/a/42909410 for the solution."""
        word = (word.encode(encoding))
        return float(crc32(word) & 0xffffffff) / 2**32


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
    Note that this need to be manually downloaded."""
    stop_words = set(stopwords.words('english'))
    text = word_tokenize(text)
    text = [word for word in text if word not in stop_words]
    return ' '.join(text)


def generate_tokens(text):
    """Tokenizes a text using Textblob, then yields a Token object."""
    tags = TextBlob(text).tags
    for word, tag in tags:
        yield Token(word, tag)


def generate_sentiment(text, type_of_sentiment: str):
    """Parses a text using textblob and returnes the semtiment (polarity) value"""
    if type_of_sentiment == 'subjectivity':
        return TextBlob(text).sentiment.subjectivity
    elif type_of_sentiment == 'polarity':
        return TextBlob(text).sentiment.polarity
    else:
        print('You need to specify what type of sentiment to generate.')
        sys.exit(-10)

