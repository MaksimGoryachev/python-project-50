#!/usr/bin/env python3
'''
This module is the entry point
'''
from gendiff.cli import parsing_args
from gendiff.diff import generate_diff


def main():
    '''
    This function is a main function.
    '''
    args = parsing_args()
    diff = generate_diff(args.first_file,
                         args.second_file,
                         args.format)
    print(diff)


if __name__ == '__main__':
    main()
