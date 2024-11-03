'''
This is a module for formatting a finished string into a stylish format.
'''


def get_indent(depth: int) -> str:
    '''
    This function returns the indentation
    '''
    return " " * (depth * 4 - 2)


def to_string(value: bool | dict | str | None, depth: int) -> str:
    '''
     This is a function for formatting string
    '''
    result = value
    if isinstance(value, bool):
        result = 'true' if value else 'false'

    elif value is None:
        result = 'null'

    elif isinstance(value, dict):
        indent = get_indent(depth)
        current_indent = indent + (" " * 6)
        lines = []
        for k, v in value.items():
            lines.append(f"{current_indent}{k}: {to_string(v, depth + 1)}")
        res = "\n".join(lines)
        result = f'{{\n{res}\n  {indent}}}'

    return result


def iter_(node: dict, depth=0) -> str:
    '''
    This is a function for formatting a finished string into a stylish format.
    '''
    children = node.get('children')
    indent = get_indent(depth)
    formatted_value = to_string(node.get('value'), depth)
    type_ = node.get('type')
    key_ = node.get('key')
    result = f"{indent}  {key_}: {formatted_value}"

    if type_ == 'root':
        lines = (iter_(child, depth + 1) for child in children)
        res = '\n'.join(lines)
        result = f'{{\n{res}\n}}'

    elif type_ == 'nested':
        lines = (iter_(child, depth + 1) for child in children)
        res = '\n'.join(lines)
        result = f"{indent}  {key_}: {{\n{res}\n  {indent}}}"

    elif type_ == 'changed':
        formatted_value1 = to_string(node.get('old_value'), depth)
        formatted_value2 = to_string(node.get('new_value'), depth)
        line1 = f"{indent}- {key_}: {formatted_value1}\n"
        line2 = f"{indent}+ {key_}: {formatted_value2}"
        result = line1 + line2

    elif type_ == 'removed':
        result = f"{indent}- {key_}: {formatted_value}"

    elif type_ == 'added':
        result = f"{indent}+ {key_}: {formatted_value}"

    return result


def formatter_stylish(node: dict) -> str:
    '''
    This is a plain output function
    '''
    return iter_(node)
