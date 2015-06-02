# -*- coding: utf-8 -*-
"""
    Useful Utils
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

import unittest
from test import test_support

import os
import string
import binascii
from base64 import b64encode, b64decode
from utilitybelt import *

base16_chars = string.hexdigits[0:16]
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


class IntToCharsetTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_int_to_deadbeef(self):
        i = 3735928559
        reference_value = ("%x" % i).replace('0x', '')
        value = int_to_charset(i, base16_chars)
        self.assertEqual(value, reference_value)

    def test_long_to_hex(self):
        i = 98593619870584680045363244857154607374163765192362173593200564555477131708560L
        reference_value = hex(i).rstrip('L').lstrip('0x')
        value = int_to_charset(i, base16_chars)
        self.assertEqual(value, reference_value)


class CharsetToIntTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_deadbeef_to_int(self):
        s = "deadbeef"
        value = charset_to_int(s, base16_chars)
        reference_value = int(s, 16)
        self.assertEqual(value, reference_value)


class Base16Tests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_int_to_hex_with_long(self):
        i = 98593619870584680045363244857154607374163765192362173593200564555477131708560L
        reference_value = hex(i)
        reference_value = reference_value.rstrip('L').lstrip('0x')
        value = int_to_hex(i)
        self.assertEqual(value, reference_value)

    def test_hex_to_int_with_64bit_string(self):
        s = "d9fa02e46cd3867f51279dfae592d3706022ee93c175b49c30c8c962722fc890"
        reference_value = int(s, 16)
        value = hex_to_int(s)
        self.assertEqual(value, reference_value)

    def test_is_int_with_long(self):
        i = 98593619870584680045363244857154607374163765192362173593200564555477131708560L
        self.assertTrue(is_int(i))

    def test_is_valid_int_with_string(self):
        i = "98593619870584680045363244857154607374163765192362173593200564555477131708560"
        self.assertTrue(is_valid_int(i))

    def test_is_hex_with_64bit_string(self):
        s = "d9fa02e46cd3867f51279dfae592d3706022ee93c175b49c30c8c962722fc890"
        self.assertTrue(is_hex(s))

    def test_hex_to_charset(self):
        s = "d9fa02e46cd3867f51279dfae592d3706022ee93c175b49c30c8c962722fc890"
        s2 = hex_to_charset(s, string.digits)
        self.assertTrue(is_valid_int(s2))

    def test_charset_to_hex(self):
        s = "98593619870584680045363244857154607374163765192362173593200564555477131708560"
        s2 = charset_to_hex(s, string.digits)
        self.assertTrue(is_hex(s2))


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
        d = {"a": {"b": {"c": "", "d": [{"e": ""}]}}}
        d = scrub_dict(d)
        self.assertEqual(len(d), 0)


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
        self.assertTrue(isinstance(d, dict))
        self.assertEqual('name' in d and d['name'], "My Class")

    def test_str_to_dict(self):
        s = "a"
        try:
            d = to_dict(a)
        except:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_int_to_dict(self):
        i = 1
        try:
            d = to_dict(i)
        except:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_dict_to_dict(self):
        d = {}
        d = to_dict(d)
        self.assertTrue(isinstance(d, dict))


class EntropyTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_dev_urandom_entropy(self):
        bytes16 = dev_urandom_entropy(16)
        self.assertEqual(len(bytes16), 16)

    def test_dev_random_entropy(self):
        bytes16 = dev_random_entropy(16)
        self.assertEqual(len(bytes16), 16)

    def test_dev_random_entropy_fallback_on_nt_operating_system(self):
        os.name = 'nt'
        bytes16 = dev_random_entropy(16)
        self.assertEqual(len(bytes16), 16)


def test_main():
    test_support.run_unittest(
        ToDictTests,
        ScrubDictTests,
        IntToCharsetTests,
        CharsetToIntTests,
        ChangeCharsetTests,
        Base16Tests,
        EntropyTests
    )

if __name__ == '__main__':
    test_main()
