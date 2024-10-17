"""
This is a parse module.
"""
from pathlib import Path
import json
import yaml
from yaml.loader import SafeLoader


def parse(file_path):
    """
    This function parse input files.
    """
    with open(file_path, 'r', encoding="utf-8") as file:
        suffix = Path(file_path).suffix
        if suffix == '.json':  # file_path.endswith('.json'):
            return json.load(file)
        if suffix in ('.yml', '.yaml'):
            return yaml.load(file, Loader=SafeLoader)

    # raise ValueError('Unknown file format')
