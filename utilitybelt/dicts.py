# -*- coding: utf-8 -*-
"""
    Utilitybelt
    ~~~~~

    :copyright: (c) 2015 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

from collections import defaultdict

""" A recursive dictionary based on the collections lib defaultdict class.
"""
recursive_dict = lambda: defaultdict(recursive_dict)


def recursive_dict_to_dict(rdict):
    """ Convert a recursive dict to a plain ol' dict.
    """
    d = {}
    for (k, v) in rdict.items():
        if isinstance(v, defaultdict):
            d[k] = recursive_dict_to_dict(v)
        else:
            d[k] = v
    return d


def scrub_dict(d):
    """ Recursively inspect a dictionary and remove all empty values, including
        empty strings, lists, and dictionaries.
    """
    if type(d) is dict:
        return dict(
            (k, scrub_dict(v)) for k, v in d.iteritems() if v and scrub_dict(v)
        )
    elif type(d) is list:
        return [
            scrub_dict(v) for v in d if v and scrub_dict(v)
        ]
    else:
        return d


def _to_json_type(obj, classkey=None):
    """ Recursively convert the object instance into a valid JSON type.
    """
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = _to_json_type(v, classkey)
        return data
    elif hasattr(obj, "_ast"):
        return _to_json_type(obj._ast())
    elif hasattr(obj, "__iter__"):
        return [_to_json_type(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([
            (key, _to_json_type(value, classkey))
            for key, value in obj.__dict__.iteritems()
            if not callable(value) and not key.startswith('_')
        ])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj


def to_dict(obj):
    """ Convert an instance of an object into a dict.
    """
    d = _to_json_type(obj)
    if isinstance(d, dict):
        return scrub_dict(d)
    else:
        raise ValueError("The value provided must be an object.")
