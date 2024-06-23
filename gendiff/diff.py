"""
This is a diff module.
"""

# import json
from gendiff.parser import parse
from gendiff.format_selector import select_formatter


def make_diff(dict1, dict2):
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


def build_diff(dict_1: dict, dict_2: dict):
    return {
        'type': 'root',
        'children': make_diff(dict_1, dict_2)
    }


def generate_diff(file1, file2, format_of_output='stylish'):
    """
    This function the generate difference function with different input files.
    """
    dict1 = parse(file1)
    dict2 = parse(file2)
    result = build_diff(dict1, dict2)
    return select_formatter(result, format_of_output)

# def json_string_conversion(data):
#     """
#     This string conversion function.
#     """
#     res = ''
#     json_str = json.dumps(data, indent=2)
#     for line in json_str.split('\n'):
#         if line.strip().endswith(','):
#             res += (line[:-1].replace('"', '')) + '\n'
#         else:
#             res += (line.replace('"', '')) + '\n'
#     res = res[:-1]
#     return res


# def get_result_dict(dict1, dict2):
#     """
#     This function is a function of generating
#     the difference between dictionaries.
#     """
#     keys = dict1.keys() | dict2.keys()
#     result_dict = {}
#     for key in sorted(keys):
#
#         if key not in dict1:
#             key_new = '+ ' + key
#             result_dict[key_new] = dict2[key]
#
#         elif key not in dict2:
#             key_new = '- ' + key
#             result_dict[key_new] = dict1[key]
#
#         elif dict1[key] == dict2[key]:
#             key_new = '  ' + key
#             result_dict[key_new] = dict1[key]
#
#         else:
#             key_new_m = '- ' + key
#             result_dict[key_new_m] = dict1[key]
#             key_new_p = '+ ' + key
#             result_dict[key_new_p] = dict2[key]
#     return result_dict
