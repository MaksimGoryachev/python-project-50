import json


def string_conversion(data):
    res = ''
    json_str = json.dumps(data, indent=2)
    for line in json_str.split('\n'):
        if line.strip().endswith(','):
            res += (line[:-1].replace('"', '')) + '\n'
        else:
            res += (line.replace('"', '')) + '\n'
    return res


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
            key_new_m = '- ' + key
            result_dict[key_new_m] = dict1[key]
            key_new_p = '+ ' + key
            result_dict[key_new_p] = dict2[key]
    return string_conversion(result_dict)
