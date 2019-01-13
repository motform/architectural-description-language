"""
4ME501 - Programming for Digital Humanities - 2019
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Stencils - pre-defined shapes used to draw cairo graphics.

There are two main types of stencils:
    Floating - Stencils that float in the surface
    Central  - Stencils that grow from the center coordinate.

The Cairo surface is normalized, which means that any
instructions have to be in the [0:1] decimal range.
"""

import parser
from helpers import str_to_float

import math
from random import Random


def handler(context, word, tag, tags):
    """Handles all the stencil definitions, keeps our code DRY.

    Once the appropriate turn of action is found in the dict,
    a stencil function is called as an inner function."""

    random = Random(hash(word))  # Deterministic randomnes
    float_word = str_to_float(word)

    def floating_triangle():
        """draws a floating triangle"""
        pass

    def floating_circle():
        """Floating Circle"""
        context.arc(random.uniform(0, 1), 0.5,  # positon
                    float_word / 2,                   # radius
                    0, 2 * math.pi)             # angle (start, end)

    def central_line():
        """Draw central_line from center and out."""
        context.move_to(0.5, 0.5)                            # x1, y1
        context.line_to(float_word, random.uniform(0, 1))  # x2, y2

    def central_arc():
        """Draws and central_arc based on the hashing of word."""
        context.arc(0.5, 0.5,                   # position
                    word / 2,                   # radius
                    random.uniform(0, 1), random.uniform(0, 1))

    def adj():
        """Handles adjectives and adverbs. When these tags are found
        we use the sentiment subjectivity to set the central_line weight,
        importance, of the next drawable word."""
        adj_sentiment = parser.generate_sentiment_subjectivity(word)
        context.set_line_width(adj_sentiment)

    tag_index = {
        # Adjectives
        'JJ':  adj(), 'JJR': adj(), 'JJS': adj(),
        # Adverbs
        'RB':  adj(), 'RBR': adj(), 'RBS': adj(),
        # Nouns
        'NN':  central_line(), 'NNS': central_line(), 'NNP': central_line(), 'NNPS': central_line(),
        # Pronoun
        'PRP': None, 'PRP$': None,
        # Verbs
        'VB':  None, 'VBD': None, 'VBG': None,
        'VBN': None, 'VBP': None, 'VBZ': None,
        # Stop-tags -> Tags we skip in the visualization
        'WDT': None, 'WP':  None, 'WP$': None, 'WRB': None,
        'SYM': None, 'TO':  None, 'UH':  None, 'RP':  None,
        'LS':  None, 'MD':  None, 'CC':  None, 'CD':  None,
        'DT':  None, 'EX':  None, 'FW':  None, 'IN':  None,
        'PDT': None, 'POS': None,
    }


    if tag_index[tag]:
        tag_index[tag]

    context.stroke()

