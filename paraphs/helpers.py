"""
4ME501 - Programming for Digital Humanities - 2019
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Various self contained helper functions.
"""

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

