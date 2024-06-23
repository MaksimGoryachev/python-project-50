from gendiff.formatters.stylish import formatter_stylish as stylish
from gendiff.formatters.plain import formatter_plain as plain
from gendiff.formatters.json import formatter_json as json


def select_formatter(diff, format_):
    formats = {
        'stylish': stylish,
        'plain': plain,
        'json': json,
    }
    if format_ in formats:
        return formats[format_](diff)

    raise ValueError(f'Unknown format: {format_}')
