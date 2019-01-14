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
from functools import wraps


def handler(context, word, tag, tags):
    """Handles all the stencil definitions, keeps our code DRY.

    Once the appropriate turn of action is found in the dict,
    a stencil function is called as an inner function."""

    float_word = str_to_float(word)
    random = Random(float_word)  # Deterministic randomnes

    # Decorators

    def central(func):
        """Deocrator of central stencils"""

        @wraps(func)
        def wrapped():
            context.save()
            context.translate(0.5, 0.5)
            func()
            context.restore()
        return wrapped

    # Stencils

    def floating_triangle():
        """Floating Triangle tba"""

    def floating_circle():
        """Floating Circle tba."""
        print('floating circle')
        context.new_sub_path()
        context.arc(random.uniform(0, 1), random.uniform(0, 1),
                    float_word / 10,                                # radius
                    0, 2 * math.pi)                                 # angle (start, end)

    @central
    def central_line():
        print('central line')
        """Draw central_line from center and out."""
        context.new_sub_path()
        context.move_to(0, 0)
        context.line_to(float_word, random.uniform(0, 1))           # x2, y2

    def central_arc():
        print('central arc')
        """Draws and central_arc based on the hashing of word."""
        context.new_sub_path()
        context.arc(0.5, 0.5,                                       # position
                    float_word / 2,                                 # radius
                    random.uniform(0.3, 1), random.uniform(0, 1))   # angle (start, end)

    def adj():
        """Handles adjectives and adverbs. When these tags are found
        we use the sentiment subjectivity to set the central_line weight,
        importance, of the next drawable word."""
        pass
        # adj_sentiment = parser.generate_sentiment_subjectivity(word)
        # context.set_line_width(adj_sentiment)

    tag_index = {
        # Adjectives
        'JJ':  adj, 'JJR': adj, 'JJS': adj,
        # Adverbs
        'RB':  adj, 'RBR': adj, 'RBS': adj,
        # Nouns
        'NN':  central_line, 'NNS':  floating_circle,
        'NNP': central_arc,  'NNPS': central_arc,
        # Pronoun
        'PRP': floating_circle, 'PRP$': None,
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

    print(word, tag)
    if tag_index[tag]:
        tag_index[tag]()  # Runs our inner function or returns False
        context.stroke()
        context.translate(0, 0)

    print()
