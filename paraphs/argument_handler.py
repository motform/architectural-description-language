"""
4ME501 - Programming for Digital Humanities - 2018
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Module that handles command line arguments.
"""

import parser

from argparse import ArgumentParser
from textwrap import dedent
import os.path
import sys


def parse_args():
    """Argparser, handles the CLI.

    For more information, refer to the Argparser Module Documentation."""
    arg_parser = ArgumentParser(prog="Paraphs",
                                description="Generates small graphical ornaments from textual inputs.\
                                             Works best on poetry, or other small texts.",
                                epilog="To change or add stencils, refer to the 'stencils' module.")

    # Positional Arguments
    arg_parser.add_argument('input', type=str,
                            help='File to read.')

    # Optional Arguments
    arg_parser.add_argument('--width', type=int, default=500,
                            help='Width of the output image. Default=500px.')
    arg_parser.add_argument('--height', type=int, default=500,
                            help='Heigh of the output image. Default=500px.')

    # Flags
    arg_parser.add_argument('-s', '--sentiment', action='store_true',
                            help='Use sentiment analysis to decide color scheme.\
                                  Negative=White on black.\
                                  Positive=Black on White.\
                                  Default=Black on White.')
    arg_parser.add_argument('-o', '--output', type=str,
                            help='Set explicit name for the output file.\
                                  Defaults to the name of the input file, suffixed with\
                                  the file extension.')
    arg_parser.add_argument('-f', '--filetype', type=str, choices=['svg', 'pdf', 'png'],
                            help='Set explicit name for the output file.\
                                  Defaults to the name of the input file, suffixed with\
                                  the file extension.')

    return arg_parser.parse_args()


def infer_output(input_file):
    """Reads name of an input and returns it sans extension."""
    input_file = os.path.basename(input_file)  # returns the file name, regardless of input path
    return input_file.split('.')[0]


def sentiment(sentiment, text):
    """Handles sentiment argument. Factored out for consistency."""
    if sentiment:
        return parser.generate_sentiment(text, type_of_sentiment='polarity')
    else:
        return 1  # Black on white


def output(filetype, output, input_file):
    """Handles output (filename) and filetype arguments.
    The program can infer missing arguments as long as filetype is provided.

    Possible cases:
    1. Valid filetype and output -> Check and return
    2. Valid filetype, no output -> Return input file name as output file name
    3. Valid Output, no filetype -> Infer filetype from output
    4. No filetype or output     -> Exit the program with helpful error
    """
    if output:
        try:
            infered_filetype = output.split('.')[1]  # Output with filename information
            if filetype and (not infered_filetype == filetype):  # There is a filetype but it does not match
                print('Error: Output inplicit filetype and explicit filetype does not match.')
                sys.exit(2)
            if not filetype:  # No filetype, infer from output
                filetype = infered_filetype
        except IndexError:  # Output name missing extension
            if filetype:  # If there is an extension, add it
                output = output + '.' + filetype
            else:
                print(dedent('Error: Invalid output file name.\
                       Enter a filetype with -f, or a complete filename with -o.'))
                sys.exit(3)
    elif filetype:  # no output, but a filetype, infer name from input
        output = infer_output(input_file) + '.' + filetype
    else:  # neither output or filename, insufficent information
        print(dedent('Error: No filetype specified.\
                      Enter a filetype with -f, or a completet filename with -o.'))
        sys.exit(4)

    return filetype, output
