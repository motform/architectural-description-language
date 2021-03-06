"""
4ME501 - Programming for Digital Humanities - 2019
Assignment 6: Final Project
Author: Love Lagerkvist (ll223jp)
Python version: 3.7

Program entry point.

For more information about Paraphs, see the
Readme or the attached report.
"""


from paraphs import parser
from paraphs import argument_handler
from paraphs import graphics


def main():
    """Entry point for the application script.

    Does the following:
    1. Reads and parses the text file with 'parser' module.
    2. Handles arguments with the 'argument_handler' module.
    3. Transfers data and control over to draw() in the 'graphics' moudule."""

    args = argument_handler.parse_args()

    # Parse text
    text = parser.read_input(args.input)
    text = parser.remove_stop_words(text)
    tokens = parser.generate_tokens(text)

    # Handle arguments
    sentiment = argument_handler.sentiment(args.sentiment, text)
    filetype, output = argument_handler.output(args.filetype, args.output, args.input)

    # Give control to the graphics moudle
    graphics.draw(tokens, output=output, filetype=filetype, sentiment=sentiment,
                  width=args.width, height=args.height)


if __name__ == '__main__':
    main()
