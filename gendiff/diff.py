"""
This is a diff module.
"""

import os
from gendiff.parser import load_and_parse_file
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
    if not os.path.isfile(path_file1):
        raise FileNotFoundError(f"File not found: {path_file1}")
    if not os.path.isfile(path_file2):
        raise FileNotFoundError(f"File not found: {path_file2}")

    dict1 = load_and_parse_file(path_file1)
    dict2 = load_and_parse_file(path_file2)

    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError("Files must contain valid data in dictionary format.")
    result = build_diff(dict1, dict2)
    return select_formatter(result, format_of_output)
