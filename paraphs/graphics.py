"""
4ME501 - Programming for Digital Humanities - 2018
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Drawing portion.
"""

import cairo
import math
import random
from zlib import crc32


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
    """Picks a color depending on text sentiment value """
    black, white = 0.0, 1.0

    if sentiment < 0:
        bg, fg = black, white
    else:
        bg, fg = white, black

    context.set_source_rgb(bg, bg, bg)
    context.rectangle(0, 0, 1, 1)  # Rectangle that covers the entire surface
    context.fill()
    context.set_source_rgb(fg, fg, fg)


def draw_line(context, word):
    """Draw line from center and out."""
    random.seed(hash(word))  # Deterministic randomnes

    hashed_word = str_to_float(word)
    context.move_to(0.5, 0.5)
    context.line_to(hashed_word, random.uniform(0, 1))
    context.stroke()


def draw_arc(context, word):
    """Draws and arc based on the hashing of word.

    A Cairo arc is defined in the following manner:
    xc, yc, radius, start angle, end angle"""
    random.seed(hash(word))  # Deterministic randomnes

    hashed_word = str_to_float(word)
    context.arc(0.5, 0.5, hashed_word / 2, random.uniform(0, 1), random.uniform(0, 1))
    context.stroke()


def hide_center(context):
    """Hides part of the center to make our ways a bit more transparent."""
    context.set_source_rgb(1, 1, 1)
    context.arc(0.5, 0.5, 20, 0, 2 * math.pi)
    context.fill()


cairo_tags = {
    'CC':  draw_line, 'CD': draw_line,
    'DT':  None,
    'EX':  None,
    'FW':  None,
    'IN':  None,
    'JJ':  draw_arc, 'JJR': draw_arc, 'JJS': draw_arc,
    'LS':  None,
    'MD':  None,
    'NN':  draw_line, 'NNS': draw_line, 'NNP': draw_line, 'NNPS': draw_line,
    'PDT': None, 'POS': None,
    'PRP': None, 'PRP$': None,
    'RB':  None, 'RBR': None, 'RBS': None,
    'RP':  None,
    'SYM': None,
    'TO':  None,
    'UH':  None,
    'VB':  None, 'VBD': None, 'VBG': None, 'VBN': None,
    'VBP': None, 'VBZ': None, 'WDT': None,
    'WP':  None, 'WP$': None, 'WRB': None,
}


def draw(tags, filename: str, width: int, height: int, sentiment=False):
    """ Main draw function.

    Tags: Some kind of iterable with tag-tuples. Our parser returns a generator.
    Filname: A string.
    Sentiment: Polarity analysis."""

    with cairo.SVGSurface(filename + '.svg', width, height) as surface:
        context = cairo.Context(surface)
        context.set_line_width(1)
        context.scale(width, height)

        if sentiment:
            sentiment_color(context, sentiment)

        for word, tag in tags:
            if cairo_tags[tag]:
                cairo_tags[tag](context, word)

# if adj
    # adj = item
    # nextiemt = next()
    # sentiment - adj
    # use nextitem with sentiment

