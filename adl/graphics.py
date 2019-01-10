"""
4ME501 - Programming for Digital Humanities - 2018
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Drawing portion.
"""

import cairo
import math
from random import randint


def draw_line(context, word, cx, cy):
    '''Draw line from center and out.'''
    hashed_word = hash(word) % 500
    context.move_to(cy, cy)
    context.line_to(hashed_word * 2, hashed_word / 2)
    context.stroke()


def draw_circle(context, word, cx, cy):
    '''Draw centralized circle.'''
    hashed_word = hash(word)
    context.arc(cx, cy, hashed_word % 200 + 40, hashed_word % 3, hashed_word % 5 + 1)
    context.stroke()


def hide_center(context, cx, cy):
    context.set_source_rgb(1, 1, 1)
    context.arc(cx, cy, 20, 0, 2 * math.pi)
    context.fill()


cairo_tags = {
        'CC'   : draw_line,
        'CD'   : 'line',
        'DT'   : 'line',
        'EX'   : 'line',
        'FW'   : 'line',
        'IN'   : 'line',
        'JJ'   : draw_circle,
        'JJR'  : 'line',
        'JJS'  : 'line',
        'LS'   : 'line',
        'MD'   : 'line',
        'NN'   : draw_line,
        'NNS'  : draw_line,
        'NNP'  : draw_line,
        'NNPS' : draw_line,
        'PDT'  : 'line',
        'POS'  : 'line',
        'PRP'  : 'line',
        'PRP$' : 'line',
        'RB'   : 'line',
        'RBR'  : 'line',
        'RBS'  : 'line',
        'RP'   : 'line',
        'SYM'  : 'line',
        'TO'   : 'line',
        'UH'   : 'line',
        'VB'   : 'line',
        'VBD'  : 'line',
        'VBG'  : 'line',
        'VBN'  : 'line',
        'VBP'  : 'line',
        'VBZ'  : 'line',
        'WDT'  : 'line',
        'WP'   : 'line',
        'WP$'  : 'line',
        'WRB'  : 'line',
        }


def draw(filename, tags, width=500, height=500):
    '''
    The main draw function.
    Expects a generator object that feeds it (word tag) tuples.
    '''

    with cairo.SVGSurface(filename + '.svg', width, height) as surface:

        context = cairo.Context(surface)
        center_x = width / 2
        center_y = height / 2
        context.set_line_width(1)

        for word, tag in tags:
            if cairo_tags[tag] == 'line':
                pass
            else:
                cairo_tags[tag](context, word, center_x, center_y)

