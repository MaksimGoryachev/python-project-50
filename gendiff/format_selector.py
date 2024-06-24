"""
    This module allows you to select the output format.
    """

from gendiff.formatters import (stylish, plain, json)


def select_formatter(diff, format_):
    """
    This function allows you to select the output format.
    """
    formats = {
        'stylish': stylish,
        'plain': plain,
        'json': json,
    }
    if format_ in formats:
        return formats[format_](diff)

    raise ValueError(f'Unknown format: {format_}')
