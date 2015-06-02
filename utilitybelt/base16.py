# -*- coding: utf-8 -*-
"""
    Utilitybelt
    ~~~~~

    :copyright: (c) 2015 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

import string
from .charsets import change_charset

B16_CHARS = string.hexdigits[0:16]
B16_REGEX = '^[0-9a-f]*$'


def hex_to_int(s):
    try:
        return int(s, 16)
    except:
        raise ValueError("Value must be in hex format")


def int_to_hex(i):
    try:
        return hex(i).rstrip('L').lstrip('0x')
    except:
        raise ValueError("Value must be in int format")


def is_hex(s):
    # make sure that s is a string
    if not isinstance(s, str):
        return False
    # if there's a leading hex string indicator, strip it
    if s[0:2] == '0x':
        s = s[2:]
    # try to cast the string as an int
    try:
        i = hex_to_int(s)
    except ValueError:
        return False
    else:
        return True


def is_int(i):
    return isinstance(i, (int,long))


def is_valid_int(i):
    if is_int(i):
        return True
    elif isinstance(i, str):
        try:
            int_i = int(i)
        except:
            return False
        else:
            return True
    return False


def hexpad(x):
    return ('0' * (len(x) % 2)) + x


def charset_to_hex(s, original_charset):
    return hexpad(change_charset(s, original_charset, B16_CHARS))


def hex_to_charset(s, destination_charset):
    if not is_hex(s):
        raise ValueError("Value must be in hex format")
    s = s.lower()
    return change_charset(s, B16_CHARS, destination_charset)
