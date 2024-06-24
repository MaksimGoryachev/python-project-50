'''
This is a module for formatting a finished string into a plain format.
'''


def to_string(value) -> str:
    '''
     This is a function for formatting string
    '''
    if isinstance(value, bool):
        return 'true' if value else 'false'

    if value is None:
        return 'null'

    if isinstance(value, dict):
        return '[complex value]'

    if isinstance(value, int):
        return value

    return f"'{value}'"


def iter_(node: dict, path="") -> str:
    '''
    This is a function for formatting a finished string into a plain format.
    '''
    children = node.get('children', [])
    key = node.get('key', '')
    current_path = f"{path}{key}"
    type_ = node.get('type')

    if type_ == 'root':
        lines = (iter_(child, path) for child in children)
        return "\n".join(filter(bool, lines))

    if type_ == 'nested':
        lines = (iter_(child, f"{current_path}.") for child in children)
        return "\n".join(filter(bool, lines))

    if type_ == 'removed':
        return f"Property '{current_path}' was removed"

    if type_ == 'added':
        formatted_value = to_string(node.get('value'))
        return (f"Property '{current_path}'"
                f" was added with value: {formatted_value}")

    if type_ == 'changed':
        formatted_old_value = to_string(node.get('old_value'))
        formatted_new_value = to_string(node.get('new_value'))
        return (f"Property '{current_path}' was updated."
                f" From {formatted_old_value} to {formatted_new_value}")


def formatter_plain(node: dict):
    '''
    This is a plain output function
    '''
    return iter_(node)
