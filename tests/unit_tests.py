# -*- coding: utf-8 -*-
"""
    Useful Utils
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

import unittest
from test import test_support

from usefulutils import recursive_dict, scrub_dict, to_dict

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
	)

if __name__ == '__main__':
    test_main()


