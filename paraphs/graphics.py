"""
4ME501 - Programming for Digital Humanities - 2019
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Module that handles the Cairo Surface and Context.
The drawing instructions are called stencils and found in that file.
"""

import stencils

import cairo
import math


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


def hide_center(context):
    """Hides part of the center to make our ways a bit more transparent."""
    context.set_source_rgb(0, 0, 0)
    context.arc(0.5, 0.5, 20, 0, 2 * math.pi)
    context.fill()


def draw(tags, filename: str, width: int, height: int, sentiment=1):
    """ Main draw function.

    Sets up a Cairo instance (surface and context), and goes
    through the words of input text. Picks the appropriate action by
    calling a dict (tag_handler) in the Stencils module."""

    with cairo.SVGSurface(filename, width, height) as surface:
        context = cairo.Context(surface)
        context.set_line_width(0.5)
        context.scale(width, height)
        sentiment_color(context, sentiment)

        for word, tag in tags:
            # Using a dict as a switch kind of thing
            stencils.handler(context, word, tag, tags)

