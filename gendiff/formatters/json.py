from json import dumps


def formatter_json(node: dict):
    return dumps(node, indent=4)
