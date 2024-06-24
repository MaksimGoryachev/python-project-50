'''
This is a module for formatting a finished string into a stylish format.
'''


def get_indent(depth: int) -> str:
    '''
    This function returns the indentation
    '''
    return " " * (depth * 4 - 2)


def to_string(value, depth: int) -> str:
    '''
     This is a function for formatting string
    '''
    if isinstance(value, bool):
        return 'true' if value else 'false'

    if value is None:
        return 'null'

    if isinstance(value, dict):
        indent = get_indent(depth)
        current_indent = indent + (" " * 6)
        lines = []
        for k, v in value.items():
            lines.append(f"{current_indent}{k}: {to_string(v, depth + 1)}")
        result = "\n".join(lines)
        return f'{{\n{result}\n  {indent}}}'

    return value


def iter_(node: dict, depth=0) -> str:
    '''
    This is a function for formatting a finished string into a stylish format.
    '''
    children = node.get('children')
    indent = get_indent(depth)
    formatted_value = to_string(node.get('value'), depth)
    formatted_value1 = to_string(node.get('old_value'), depth)
    formatted_value2 = to_string(node.get('new_value'), depth)
    type_ = node.get('type')
    key_ = node.get('key')

    if type_ == 'root':
        lines = (iter_(child, depth + 1) for child in children)
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'

    if type_ == 'nested':
        lines = (iter_(child, depth + 1) for child in children)
        result = '\n'.join(lines)
        return f"{indent}  {key_}: {{\n{result}\n  {indent}}}"

    if type_ == 'changed':
        line1 = f"{indent}- {key_}: {formatted_value1}\n"
        line2 = f"{indent}+ {key_}: {formatted_value2}"
        return line1 + line2

    if type_ == 'unchanged':
        return f"{indent}  {key_}: {formatted_value}"

    if type_ == 'removed':
        return f"{indent}- {key_}: {formatted_value}"

    if type_ == 'added':
        return f"{indent}+ {key_}: {formatted_value}"


def formatter_stylish(node: dict):
    '''
    This is a plain output function
    '''
    return iter_(node)
