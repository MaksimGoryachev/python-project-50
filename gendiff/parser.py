"""
This is a parse module.
"""
from pathlib import Path
import json
import yaml
from yaml.loader import SafeLoader


def read_file(file):
    """
    This function return data from a file.
    """
    with open(file, 'r', encoding="utf-8") as f:
        return f.read()


def parse(data):
    """
    This function parse input data.
    """
    if Path(data).is_file():
        file_content = read_file(data)
        suffix = Path(data).suffix
        if suffix == '.json':
            return json.loads(file_content)
        if suffix in ('.yml', '.yaml'):
            return yaml.load(file_content, Loader=SafeLoader)
    return data  # Если это не файл, возвращаем данные как есть
