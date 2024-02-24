#!/usr/bin/python3
"""Defines a function that returns the JSON representation
of an object(string)"""
import json


def to_json_string(my_obj):
    """Serializes object to JSON format

    Args:
        my_obj: The object to be serialized

    Returns:
        The JSON representation of an object
    """
    return json.dumps(my_obj)
