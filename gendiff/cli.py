"""
This is a Parser module.
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
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
