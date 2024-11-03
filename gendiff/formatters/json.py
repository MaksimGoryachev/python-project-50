'''
This is a module for formatting a finished string into a json format.
'''


from json import dumps


def formatter_json(node: dict) -> str:
    '''
    This is a json output function
    '''
    return dumps(node, indent=4)
