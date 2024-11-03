"""
    This module allows you to select the output format.
    """

from gendiff.formatters import (stylish, plain, json)


def select_formatter(diff, format_: str):
    """
    This function allows you to select the output format.
    """
    formats = {
        'stylish': stylish,
        'plain': plain,
        'json': json,
    }
    return formats[format_](diff)
