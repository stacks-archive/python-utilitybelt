# -*- coding: utf-8 -*-
"""
    Utilitybelt
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

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


