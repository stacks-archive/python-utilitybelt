# -*- coding: utf-8 -*-
"""
    Utilitybelt
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

import os
import binascii


def dev_urandom_entropy(numbytes):
    """ Reads random bytes from the /dev/urandom pool.

        NOTE: /dev/urandom is a non-blocking pseudorandom number generator.
        If the entropy pool runs out, previously released entropy will be used.
        If blocking is unnacceptable, use this over "dev_urandom_entropy".
    """
    return os.urandom(numbytes)


def dev_random_entropy(numbytes, fallback_to_urandom=True):
    """ Reads random bytes from the /dev/random entropy pool.

        NOTE: /dev/random is a blocking pseudorandom number generator.
        If the entropy pool runs out, this function will block until more
        environmental noise is gathered.
        If entropy re-use is unnacceptable use this over "dev_urandom_entropy".

        If "fallback_to_urandom" is set, this function will fallback to
        /dev/urandom on operating systems without /dev/random.
    """
    if os.name == 'nt' and fallback_to_urandom:
        return dev_urandom_entropy(numbytes)
    return open("/dev/random", "rb").read(numbytes)
