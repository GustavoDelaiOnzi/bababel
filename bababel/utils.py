import json
import re


def dict_to_bytes(body: dict) -> bytes:
    """
    Convert a given dict to bytes.

    :param body: Dictionary to be converted to bytes.
    :return: Byte representation of the dictionary.
    """
    json_str = json.dumps(body)
    return json_str.encode("utf-8")


def camel_to_snake(name: str) -> str:
    """
    Gets a CamelCase string and transform to a SnakeCase string.
    :param name: CamelCase case string.
    :return: snake_case string.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
