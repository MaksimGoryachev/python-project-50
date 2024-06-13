#!/usr/bin/env python3
from gendiff.cli import parsing_args
from gendiff.diff import generate_diff


def main():
    first_file, second_file = parsing_args()
    diff = (generate_diff(first_file, second_file))
    print(diff)


if __name__ == '__main__':
    main()
