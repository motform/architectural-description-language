"""
4ME501 - Programming for Digital Humanities - 2019
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Stencils - pre-defined shapes used to draw cairo graphics.
This is not a fun file to read. The stencil definitons are
all very specific drawing instructions for Cairo, and can be
quite hard to work with if you are not used to the way it works.

Stencils are either drawn filled our outlined. This is
controlled by decorators on a per-stencil basis.

There are two main types of stencils:
    Floating - Stencils that float in the surface
    Central  - Stencils that grow from the center coordinate.

At one point the the process, positional attributes where also
decorated using the 'context.translate'-method. However, this
prooved to introduce more complexicy than it reduced, and as such,
it was factored back into the separate stencils.

The Cairo surface is normalized, which means that any
instructions have to be in the [0:1] decimal range.

Arc and rectangle based functions have rudamentary bounds checking,
to stop them from breaking the image frame.
"""

from paraphs import graphics

import math


# Decorators


def fill(func):
    """Decorator - renders stencil filled."""
    def draw_with_fill(*args, **kwargs):
        func(*args, **kwargs)
        graphics.context.fill()
    return draw_with_fill


def stroke(func):
    """Decorator - renders stencil as an outline (stroke only)."""
    def draw_with_stroke(*args, **kwargs):
        func(*args, **kwargs)
        graphics.context.stroke()
    return draw_with_stroke


# Stencils

@fill
def floating_row_rectangles(token):
    """Stencil - a row of regularly shaped rectangles. Number of rectangles
    are chosen from the first decimal digit of the word value."""
    iterations = int(str(token.value)[2])
    x1 = token.uniform(0, 1)
    y1 = x1  # veritcal axis, always the same
    x2, y2 = token.uniform(0.01, 0.02), token.uniform(0.03, 0.04)

    for i in range(1, iterations + 1):
        if (x1 + x2) >= 1 or (x1 + y2) >= 1:
            break  # Bounds checking

        graphics.context.rectangle(x1, y1, x2, y2)  # x1 y1 x2 y2
        x1 += 0.03


@fill
def floating_triangle(token):
    """Stincil - A single floating triangle. Due to the imperative nature of
    cairo, they all face the same direction."""
    a, b = token.uniform(0.1, 0.3), token.uniform(0.1, 0.3)

    if (token.value) >= 1 or (token.value + a) >= 1 or (a) >= 1 or (b) >= 1:
        return  # Bounds checking

    graphics.context.move_to(token.value, a)
    graphics.context.line_to(token.value, b)
    graphics.context.line_to(token.value + a, b)


@fill
def floating_teardrop(token):
    """Stencil - A single floating teardrop shape. More or less a triangle
    out of order and with a curve."""
    a, b = token.uniform(0, 0.5), token.uniform(0, 0.5)

    if (token.value) >= 1 or (token.value + a) >= 1 or (a) >= 1 or (b) >= 1:
        return  # Bounds checking

    graphics.context.line_to(token.value + a, b)
    graphics.context.line_to(token.value, b)
    graphics.context.move_to(token.value, a)
    graphics.context.curve_to(token.value + a, b, token.value, b, token.value, a)


@fill
def floating_circle(token):
    """Stencil - A floating circle, nothing more nothing less."""
    x, y = token.uniform(0, 1), token.uniform(0, 1)
    radius = token.value / 50 + 0.01  # Small, but not too small

    if (x + radius) >= 1 or (y + radius) >= 1 or radius > y or radius > x:
        return  # Bounds checking

    graphics.context.arc(x, y, radius, 0, 2 * math.pi)


@fill
def floating_semi_circle(token):
    """Stencil - A floating semi-circle. A circle cut in a little more than half."""
    x, y = token.uniform(0, 1), token.uniform(0, 1)
    radius = token.value / 25 + 0.01

    if (x + radius) >= 1 or (y + radius) >= 1:
        return  # Bounds checking

    graphics.context.arc(x, y, radius, math.pi, token.uniform(0, 1))


@stroke
def floating_line(token):
    """Stencil - A floating line. Will connect to pre/proceeding lines/curves."""
    graphics.context.move_to(token.uniform(0, 1), token.uniform(0, 1))
    graphics.context.line_to(token.value, token.value)


@stroke
def floating_curve(token):
    """Stencil - A floting curve. Will connect to pre/proceeding lines/curves."""
    graphics.context.move_to(token.value, token.value)
    graphics.context.curve_to(token.uniform(0, 1), token.uniform(0, 1),
                              token.uniform(0, 1), token.uniform(0, 1),
                              token.uniform(0, 1), token.uniform(0, 1))


@stroke
def central_line(token):
    """Stencil - A line from center and out. Will connect to pre/proceeding lines/curves."""
    graphics.context.move_to(0.5, 0.5)
    graphics.context.line_to(token.uniform(0, 1), token.value)


@stroke
def central_arc(token):
    """Stencil - An arch whose central point is the center of the surface."""
    graphics.context.arc(0.5, 0.5, token.value / 2, token.uniform(0, 1), token.uniform(0, 1))


# Compound Stencils

def compound_path(token):
    """An adverb is a very simple compound path."""
    floating_curve(token)
    floating_line(token)


# Word Tags

def adjective(token):
    """Adjectives set line width for all succeding stencils."""
    graphics.context.set_line_width(token.uniform(0.001, 0.01))


# rare verbs yield complex figures
rare_verb = [floating_row_rectangles, floating_row_rectangles,
             floating_teardrop]

# nouns yield filled shapes
noun = [floating_triangle, floating_triangle,
        floating_circle,   floating_circle,
        floating_circle,   floating_circle,
        floating_semi_circle]

# verbs yield single lines
verb = [central_line,   central_line,
        central_arc,    central_arc,
        floating_line,  floating_line,
        floating_curve, floating_curve]

adverb = [compound_path, compound_path]

tag_index = {
    'VB':  verb,      'VBD':  rare_verb, 'VBG': verb,
    'VBN': verb,      'VBP':  verb,      'VBZ': rare_verb,
    'RB':  adverb,    'RBR':  adverb,    'RBS': adverb,
    'JJ':  adjective, 'JJR':  adjective, 'JJS': adjective,
    'NN':  noun,      'NNS':  noun,      'NNP': noun,      'NNPS': noun,
    'WDT': None,      'WP':   None,      'WP$': None,      'WRB':  None,
    'SYM': None,      'TO':   None,      'UH':  None,      'RP':   None,
    'LS':  None,      'MD':   None,      'CC':  None,      'CD':   None,
    'DT':  None,      'EX':   None,      'FW':  None,      'IN':   None,
    'PDT': None,      'POS':  None,      'PRP': None,      'PRP$': None,
}

