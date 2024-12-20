"""
This module provides a command-line argument
parser for comparing two configuration files.
"""

import argparse


def parsing_args():
    """
    This function parsing args from command line.
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format',
                        choices=['stylish', 'plain', 'json'],
                        default='stylish',
                        help='set format of output', type=str)
    return parser.parse_args()
