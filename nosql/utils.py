# -*- coding: UTF8 -*-

import json

from time import time
from hashlib import md5


def encode_json(dictionary: dict) -> str:
    """
    Takes a dictionary and returns a JSON-encoded string.

    :param dict dictionary: A dictionary.
    :return str: A JSON-encoded string.
    """
    return json.JSONEncoder().encode(dictionary)


def decode_json(json_string: str) -> dict:
    """
    Takes a message as a JSON string and unpacks it to get a dictionary.

    :param str json_string: A message, as a JSON string.
    :return dict: An unverified dictionary. Do not trust this data.
    """
    return json.JSONDecoder().decode(json_string)


def hash_iterable(iterable) -> str:
    if type(iterable) == bytes:
        b = iterable
    else:
        b = "".join(str(i) for i in iterable).encode('utf-8')
    m = md5()
    m.update(b)
    m.update(str(time()).encode('utf-8'))
    return m.hexdigest()
