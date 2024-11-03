"""
    This module provides functions to generate differences between two dictionaries.
    """

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
