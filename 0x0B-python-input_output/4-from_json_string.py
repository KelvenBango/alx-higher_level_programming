#!/usr/bin/python3
"""Defines a function that returns an object (Python data structure)
represented by a JSON string"""
import json


def from_json_string(my_str):
    """Parse object to JSON format.

    Args:
        my_str (str): object
    """

    return json.loads(my_str)
