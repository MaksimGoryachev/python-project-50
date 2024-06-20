"""
This is a diff module.
"""

import json
from gendiff.parser import parse


def json_string_conversion(data):
    """
    This string conversion function.
    """
    res = ''
    json_str = json.dumps(data, indent=2)
    for line in json_str.split('\n'):
        if line.strip().endswith(','):
            res += (line[:-1].replace('"', '')) + '\n'
        else:
            res += (line.replace('"', '')) + '\n'
    res = res[:-1]
    return res


def generate_diff(file1, file2):
    """
    This function the generate difference function with different input files.
    """
    dict1 = parse(file1)
    dict2 = parse(file2)
    result_dict = get_result_dict(dict1, dict2)
    return json_string_conversion(result_dict)


def get_result_dict(dict1, dict2):
    """
    This function is a function of generating
    the difference between dictionaries.
    """
    keys = dict1.keys() | dict2.keys()
    result_dict = {}
    for key in sorted(keys):

        if key not in dict1:
            key_new = '+ ' + key
            result_dict[key_new] = dict2[key]

        elif key not in dict2:
            key_new = '- ' + key
            result_dict[key_new] = dict1[key]

        elif dict1[key] == dict2[key]:
            key_new = '  ' + key
            result_dict[key_new] = dict1[key]

        else:
            key_new_m = '- ' + key
            result_dict[key_new_m] = dict1[key]
            key_new_p = '+ ' + key
            result_dict[key_new_p] = dict2[key]
    return result_dict
