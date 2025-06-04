#!/usr/bin/env python3
"""
A simple command-line program to sort numbers.

Usage: python sort_numbers.py <number1> <number2> ... <numberN>
Example: python sort_numbers.py 5 2 8 1 9 3
"""

import sys
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Sort numbers provided as command-line arguments",
        epilog="Example: python sort_numbers.py 5 2 8 1 9 3"
    )
    parser.add_argument(
        'numbers',
        nargs='+',
        type=float,
        help='Numbers to sort (can be integers or floats)'
    )
    parser.add_argument(
        '--reverse',
        action='store_true',
        help='Sort in descending order'
    )
    parser.add_argument(
        '--output-format',
        choices=['line', 'space', 'comma'],
        default='space',
        help='Output format: line (one per line), space (space-separated), comma (comma-separated)'
    )

    try:
        args = parser.parse_args()
    except SystemExit:
        return 1

    # Sort the numbers
    sorted_numbers = sorted(args.numbers, reverse=args.reverse)

    # Format output based on user preference
    if args.output_format == 'line':
        for num in sorted_numbers:
            print(f"{num:g}")  # :g removes unnecessary decimal places
    elif args.output_format == 'comma':
        print(', '.join(f"{num:g}" for num in sorted_numbers))
    else:  # space separated (default)
        print(' '.join(f"{num:g}" for num in sorted_numbers))

    return 0


if __name__ == "__main__":
    sys.exit(main()) 