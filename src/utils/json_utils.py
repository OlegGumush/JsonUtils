from json import JSONDecoder
from json import JSONEncoder


class _JSONEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def to_dict(obj: any):
    return JSONDecoder().decode(_JSONEncoder().encode(obj))


def to_json(obj: any):
    return _JSONEncoder().encode(obj)


def json_to_dict(json: str):
    return JSONDecoder().decode(json)


def dict_to_json(dictionary: dict):
    return _JSONEncoder().encode(dictionary)


def contains(expected: dict, actual: dict):
    return expected.items() <= actual.items()
