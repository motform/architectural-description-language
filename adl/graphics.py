"""
4ME501 - Programming for Digital Humanities - 2018
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Drawing portion.
"""

import cairo
import math
from zlib import crc32


class ContextHandler(object):
    """Handles context-obejct
    semi pointless class really"""

    def __init__(self, context, width, height):
        self.context = context
        self.height = height
        self.width = width

        # We set the context scale == w*h, in order to normalize the coordinates
        self.context.scale(self.width, self.height)
        self.center = 0.5


def str_to_float(word, encoding="utf-8"):
    """The Cairo context is normalised to a [0:1] scale.
    This helps out with the drawing functions, but makes hash()
    inadaquite, as it only outputs integers. Instead, we use a crc32
    function to make normalised and unsigned floats in our range.

    The Python std:lib implementation of crc32 requires bytestrings,
    which is why we include an explicit conversion step.

    Credit to https://stackoverflow.com/a/42909410 for the solution."""
    word = (word.encode(encoding))
    return float(crc32(word) & 0xffffffff) / 2**32


def sentiment_color(context, sentiment):
    """Picks a color depending on text sentiment value

    Banal AND badly implemented!"""
    context.context.rectangle(0, 0, 1, 1)  # Rectangle that covers the entire surface

    if sentiment < -0.5:
        context.context.set_source_rgba(1, 1, 1, 1)
        context.context.fill()
        context.context.set_source_rgba(0, 0, 0, 1)
    elif sentiment <= 0:
        context.context.set_source_rgba(0.5, 0.5, 0.5, 1)
        context.context.fill()
        context.context.set_source_rgba(1, 1, 1, 1)
    elif sentiment <= 0.5:
        context.context.set_source_rgba(0.5, 0.5, 0.5, 1)
        context.context.fill()
        context.context.set_source_rgba(0, 0, 0, 1)
    else:
        context.context.set_source_rgba(0, 0, 0, 1)
        context.context.fill()
        context.context.set_source_rgba(1, 1, 1, 1)


def draw_line(context, word):
    """Draw line from center and out."""
    hashed_word = str_to_float(word)
    context.context.move_to(context.center, context.center)
    context.context.line_to(hashed_word * 2, hashed_word / 2)
    context.context.stroke()


def draw_arc(context, word):
    """Draw centralized circle.

    A Cairo arc is defined in the following manner:
    cx, cy, r, start, finish"""
    hashed_word = str_to_float(word)
    context.context.arc(context.center, context.center, hashed_word, hashed_word, hashed_word + 0.4)
    context.context.stroke()


def hide_center(context):
    """Hides part of the center to make our ways a bit more transparent."""
    context.set_source_rgb(1, 1, 1)
    context.arc(context.center, context.center, 20, 0, 2 * math.pi)
    context.fill()


cairo_tags = {
        'CC':  draw_line, 'CD': draw_line,
        'DT':  False,
        'EX':  False,
        'FW':  False,
        'IN':  False,
        'JJ':  draw_arc, 'JJR': draw_arc, 'JJS': draw_arc,
        'LS':  False,
        'MD':  False,
        'NN':  draw_line, 'NNS': draw_line, 'NNP': draw_line, 'NNPS': draw_line,
        'PDT': False, 'POS': False,
        'PRP': False, 'PRP$': False,
        'RB':  False, 'RBR': False, 'RBS': False,
        'RP':  False,
        'SYM': False,
        'TO':  False,
        'UH':  False,
        'VB':  False, 'VBD': False, 'VBG': False, 'VBN': False,
        'VBP': False, 'VBZ': False, 'WDT': False,
        'WP':  False, 'WP$': False, 'WRB': False,
}


def draw(tags, filename: str, width: int, height: int, sentiment=False):
    """ Main draw function.

    Tags: Some kind of iterable with tag-tuples. Our parser returns a generator.
    Filname: A string.
    Sentiment: Polarity analysis."""

    with cairo.SVGSurface(filename + '.svg', width, height) as surface:

        context = cairo.Context(surface)
        context = ContextHandler(context, width, height)
        context.context.set_line_width(1)
        sentiment_color(context, sentiment)

        for word, tag in tags:
            if cairo_tags[tag]:
                cairo_tags[tag](context, word)
