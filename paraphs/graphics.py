"""
4ME501 - Programming for Digital Humanities - 2019
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Module that handles the Cairo Surface and Context.
The drawing instructions are called stencils and found in that file.
"""

from paraphs import stencils

import cairo


def sentiment_color(context, sentiment):
    """Picks a color depending on text sentiment value.

    If not value is suppplied, it defualts to black on white."""
    if sentiment < 0:  # Negative sentiment == white pen on black background
        bg, fg = 0.0, 1.0
    else:  # Positive sentiment == white pen on black background
        bg, fg = 1.0, 0.0

    context.set_source_rgb(bg, bg, bg)  # Set the background color
    context.rectangle(0, 0, 1, 1)  # Rectangle that covers the entire surface
    context.fill()
    context.set_source_rgb(fg, fg, fg)  # Set our pen color


def draw(tags, output: str, filetype: str, width: int, height: int, sentiment=1):
    """ Main draw function.

    Sets up a Cairo instance (surface and context), and goes through the
    word-tag-tuples of input text. Picks the appropriate action by calling a
    dict (tag_handler) in the Stencils module."""

    if filetype == 'svg':
        surface = cairo.SVGSurface(output, width, height)
    elif filetype == 'pdf':
        surface = cairo.PDFSurface(output, width, height)
    elif filetype == 'png':
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)

    context = cairo.Context(surface)
    context.scale(width, height)
    context.set_line_width(0.007)
    context.set_line_join(cairo.LINE_JOIN_ROUND)
    context.set_line_cap(cairo.LINE_CAP_ROUND)
    sentiment_color(context, sentiment)

    for word, tag in tags:
        stencils.handler(context, word, tag)

    if filetype == 'png':  # Cairo requires bitmaps to be explicitly written
        surface.write_to_png(output)
