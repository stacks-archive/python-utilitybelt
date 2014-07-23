# -*- coding: utf-8 -*-
"""
    Useful Utils
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

import unittest
from test import test_support

import string, binascii
from base64 import b64encode, b64decode
from usefulutils import recursive_dict, scrub_dict, to_dict, \
	charset_to_int, int_to_charset, change_charset

base16_chars = string.hexdigits[0:16]
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

class IntToCharsetTests(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_int_to_deadbeef(self):
		i = 3735928559
		assert(("0x%x" % i).replace('0x', '') == int_to_charset(i, base16_chars))

class CharsetToIntTests(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_deadbeef_to_int(self):
		s = "deadbeef"
		assert(int(s, 16) == charset_to_int(s, base16_chars))

class ChangeCharsetTests(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

class ScrubDictTests(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_nested_dict(self):
		d = { "a": { "b": { "c": "", "d": [{"e": ""}] } } }
		d = scrub_dict(d)
		assert(len(d) == 0)

class ToDictTests(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass
		
	def test_class_instance_to_dict(self):
		class Thing():
			def __init__(self):
				self.name = "My Class"
		thing = Thing()
		d = to_dict(thing)
		assert(isinstance(d, dict))
		assert('name' in d and d['name'] == "My Class")

	def test_str_to_dict(self):
		s = "a"
		try:
			d = to_dict(a)
		except:
			assert(True)
		else:
			assert(False)

	def test_int_to_dict(self):
		i = 1
		try:
			d = to_dict(i)
		except:
			assert(True)
		else:
			assert(False)

	def test_dict_to_dict(self):
		d = {}
		d = to_dict(d)
		assert(isinstance(d, dict))

def test_main():
	test_support.run_unittest(
		ToDictTests,
		ScrubDictTests,
		IntToCharsetTests,
		CharsetToIntTests,
		ChangeCharsetTests
	)

if __name__ == '__main__':
    test_main()


