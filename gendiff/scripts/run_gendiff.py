#!/usr/bin/env python3
from gendiff.cli import parsing_args
from gendiff.diff import generate_diff


def main():
    first_file, second_file, format_of_output = parsing_args()
    diff = generate_diff(first_file, second_file, format_of_output)
    print(diff)


if __name__ == '__main__':
    main()
