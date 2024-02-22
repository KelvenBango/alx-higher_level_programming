#!/usr/bin/python3
"""Defines an object attributes lookup function."""


def lookup(obj):
    """Return a list of an objects available attributes."""
    return dir(obj)
