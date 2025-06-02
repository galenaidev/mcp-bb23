#!/usr/bin/env python3
"""
A simple command-line program that sorts numbers provided as arguments.

Usage: python sort_numbers.py [numbers...]
Example: python sort_numbers.py 5 2 8 1 9 3
"""

import sys
import argparse


def sort_numbers(numbers):
    """Sort a list of numbers and return the sorted list."""
    try:
        # Convert string arguments to floats for proper numerical sorting
        num_list = [float(num) for num in numbers]
        return sorted(num_list)
    except ValueError as e:
        print(f"Error: Invalid number format. {e}")
        sys.exit(1)


def main():
    """Main function to handle command-line arguments and sort numbers."""
    parser = argparse.ArgumentParser(
        description="Sort numbers provided as command-line arguments",
        epilog="Example: python sort_numbers.py 5 2 8 1 9 3"
    )
    parser.add_argument(
        'numbers',
        nargs='*',
        help='Numbers to sort (space-separated)'
    )
    parser.add_argument(
        '-r', '--reverse',
        action='store_true',
        help='Sort in descending order'
    )
    
    args = parser.parse_args()
    
    if not args.numbers:
        print("Please provide numbers to sort.")
        print("Usage: python sort_numbers.py [numbers...]")
        print("Example: python sort_numbers.py 5 2 8 1 9 3")
        sys.exit(1)
    
    # Sort the numbers
    sorted_numbers = sort_numbers(args.numbers)
    
    # Reverse if requested
    if args.reverse:
        sorted_numbers.reverse()
    
    # Display results
    print("Original numbers:", ' '.join(args.numbers))
    print("Sorted numbers:  ", ' '.join(map(str, sorted_numbers)))


if __name__ == "__main__":
    main() 