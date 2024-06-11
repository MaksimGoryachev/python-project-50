#!/usr/bin/env python3
from gendiff.cli import parsing_args
from gendiff.diff import generate_diff
import json


def string_conversion(data):
    json_str = json.dumps(data, indent=2)
    for line in json_str.split('\n'):
        if line.strip().endswith(','):
            print(line[:-1].replace('"', ''))
        else:
            print(line.replace('"', ''))

def main():
    first_file, second_file = parsing_args()
    diff = (generate_diff(first_file, second_file))
    string_conversion(diff)


if __name__ == '__main__':
    main()
