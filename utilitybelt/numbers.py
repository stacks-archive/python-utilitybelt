# -*- coding: utf-8 -*-
"""
    Utilitybelt
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

def is_hex(val):
    if val[0:2] == '0x':
        val = val[2:]
    try:
        int(val, 16)
    except ValueError:
        return False
    else:
        return True

def is_int(val):
    return isinstance(val, int)

def hex_to_int(s):
    if s[0:2] == '0x':
        s = s[2:]
	try:
		return int(s, 16)
	except:
		raise ValueError("Value must be in hex format")

def int_to_hex(val):
	try:
		return hex(val)[2:]
	except:
		raise ValueError("Value must be in int format")
