"""
This is a diff module.
"""

from gendiff.parser import parse
from gendiff.formatters import (stylish, plain, json)
from gendiff.diff_generator import build_diff


def select_formatter(diff, format_name: str):
    """
    This function allows you to select the output format.
    """
    formats = {
        'stylish': stylish,
        'plain': plain,
        'json': json,
    }
    if format_name not in formats:
        raise ValueError(f"Unsupported format: {format_name}")
    return formats[format_name](diff)


def generate_diff(path_file1: str,
                  path_file2: str,
                  format_of_output: str = 'stylish'):
    """
    This function the generate difference function with different input files.
    """
    dict1 = parse(path_file1)
    dict2 = parse(path_file2)
    result = build_diff(dict1, dict2)
    return select_formatter(result, format_of_output)
