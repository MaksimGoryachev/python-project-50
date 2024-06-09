import json


def generate_diff(file1, file2):
    with open(file1) as f1:
        dict1 = json.load(f1)
    with open(file2) as f2:
        dict2 = json.load(f2)
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
            key_newm = '- ' + key
            result_dict[key_newm] = dict1[key]
            key_newp = '+ ' + key
            result_dict[key_newp] = dict2[key]
    return result_dict