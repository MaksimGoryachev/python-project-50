"""
This is a diff module.
"""

from gendiff.parser import parse
from gendiff.format_selector import select_formatter


def make_diff(dict1: dict, dict2: dict) -> dict:
    """
    This function is a function of generating
    the difference between dictionaries.
    """
    keys = dict1.keys() | dict2.keys()
    result_list = []
    for key in sorted(keys):
        child1 = dict1.get(key)
        child2 = dict2.get(key)

        if key not in dict1:
            result_list.append({'key': key,
                                'type': 'added',
                                'value': child2
                                })
        elif key not in dict2:
            result_list.append({'key': key,
                                'type': 'removed',
                                'value': child1
                                })
        elif isinstance(child1, dict) and isinstance(child2, dict):
            result_list.append({'key': key,
                                'type': 'nested',
                                'children': make_diff(child1, child2)
                                })
        elif child1 != child2:
            result_list.append({'key': key,
                                'type': 'changed',
                                'old_value': child1,
                                'new_value': child2
                                })
        else:
            result_list.append({'key': key,
                                'type': 'unchanged',
                                'value': child1
                                })

    return result_list


def build_diff(dict1: dict, dict2: dict) -> dict:
    '''
    This function is a function of generating
    '''
    return {
        'type': 'root',
        'children': make_diff(dict1, dict2)
    }


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
