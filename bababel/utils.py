import json
import re

from bababel.exceptions import BababelValueError


def dict_to_bytes(body: dict) -> bytes:
    json_str = json.dumps(body)
    return json_str.encode("utf-8")


def camel_to_snake(name: str) -> str:
    """
    Gets a CamelCase string and transform to a SnakeCase string.
    :param name: CamelCase case string.
    :return: snake_case string.
    """
    if not is_camel_case(name):
        raise BababelValueError("'name' param expected to be a CamelCase")
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


def is_camel_case(name: str) -> bool:
    """
    Checks if a string is CamelCase or not.
    :param name: CamelCase string.
    :return: Boolean.
    """
    return bool(re.fullmatch(r'[A-Z][a-zA-Z0-9]*', name))
