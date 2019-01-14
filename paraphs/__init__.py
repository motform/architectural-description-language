"""
4ME501 - Programming for Digital Humanities - 2019
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Program entry point.
Handles arguments and input text handling.
"""


import parser
import graphics

from argparse import ArgumentParser


def parse_args():
    """Argparser, handles the CLI.

    For more information, refer to the Argparser Module Documentation."""
    arg_parser = ArgumentParser(prog="Paraphs",
                                description="Generates small graphical ornaments from textual inputs.\
                                             Works best on poetry, or other small texts.",
                                epilog="To change or add stencils, refer to the 'stencils' module.")

    # Positional Arguments
    arg_parser.add_argument('file', type=str,
                            help='File to read.')

    # Optional Arguments
    arg_parser.add_argument('-width', type=int, default=500,
                            help='Width of the output image.')
    arg_parser.add_argument('-height', type=int, default=500,
                            help='Heigh of the output image.')

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

    return arg_parser.parse_args()


def main(args):
    """Entry point for the application script.

    Does the following:
    1. Reads and parses the text file with Parser module.
    2. Handles arguments.
    3. Transfers data and control over to graphcs.draw()."""

    text = parser.read_file(args.file)
    text = parser.remove_stop_words(text)
    tags = parser.generate_tags(text)

    if args.sentiment:
        sentiment = parser.generate_sentiment_polarity(text)
    else:
        sentiment = 1  # Black on white

    if args.output:
        try:
            if args.output.split('.')[1]:
                filename = args.output
        except IndexError:
            filename = args.output + '.svg'
    else:
        filename = parser.get_filename(args.file)

    graphics.draw(tags, filename=filename, sentiment=sentiment, width=args.width, height=args.height)


if __name__ == '__main__':
    main(parse_args())
