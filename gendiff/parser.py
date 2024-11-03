"""
This is a parse module.
"""
from pathlib import Path
import json
import yaml
from yaml.loader import SafeLoader


def read_file(path_file: str) -> str:
    """
    This function return data from a file.
    """
    with open(path_file, 'r', encoding="utf-8") as f:
        return f.read()


def load_and_parse_file(file_path: str):
    """
    This function reads data from a file
    and parses it based on the file extension.
    """
    if Path(file_path).is_file():
        file_content = read_file(file_path)
        suffix = Path(file_path).suffix.lower()
        return parse(file_content, suffix)
    if Path(file_path).is_dir():
        return (f"Error: the directory is specified"
                f" instead of the data: {file_path}")


def parse(data, format_name):
    """
    This function parse input data.
    """
    if format_name == '.json':
        return json.loads(data)
    if format_name in ('.yml', '.yaml'):
        return yaml.load(data, Loader=SafeLoader)

    raise ValueError(f'Unsupported format: {format_name}.'
                     f'Supported formats are .json, .yml, .yaml.')
