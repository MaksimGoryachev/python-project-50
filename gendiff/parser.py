import json
import yaml
from yaml.loader import SafeLoader


def parse(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        if file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.load(file, Loader=SafeLoader)

    raise ValueError('Unknown file format')
