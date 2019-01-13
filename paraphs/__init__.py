"""
4ME501 - Programming for Digital Humanities - 2019
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Tools for parsing texts, using TextBlob
"""


import parser
import graphics
from argparse import ArgumentParser


def main():
    """Entry point for the application script."""

    text = '''
           Over the last 50 years, our world has turned digital at breakneck speed.
           No art form has captured this transitional time period - our time period
           - better than generative art. Generative art takes full advantage of
           everything that computing has to offer, producing elegant and compelling
           artworks that extend the same principles and goals artists have pursued
           from the inception of modern art.
           '''

    text = parser.remove_stop_words(text)
    tags = parser.generate_tags(text)
    text_sentiment = parser.generate_sentiment_polarity(text)
    graphics.draw(tags, filename='test', sentiment=text_sentiment, width=500, height=500)


if __name__ == '__main__':
    main()
