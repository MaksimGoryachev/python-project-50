#!/usr/bin/env python3
'''
This module is the entry point
'''
import sys

from gendiff.cli import parsing_args
from gendiff.diff import generate_diff


def main():
    '''
    This function is a main function.
    '''
    try:
        args = parsing_args()
        diff = generate_diff(args.first_file,
                             args.second_file,
                             args.format)
        print(diff)
    except ValueError as err:
        print(err)
        sys.exit(1)
    except OSError:
        print('Какая-то ошибка системы')
        sys.exit(1)


if __name__ == '__main__':
    main()
