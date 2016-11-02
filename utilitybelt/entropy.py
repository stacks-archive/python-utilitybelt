# -*- coding: utf-8 -*-
"""
    Utilitybelt
    ~~~~~

    :copyright: (c) 2015 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

import os
import fcntl
import select
import time
import binascii
import random

class OutOfEntropyException(Exception):
    pass

def dev_urandom_entropy(numbytes):
    """ Reads random bytes from the /dev/urandom pool.

        NOTE: /dev/urandom is a non-blocking pseudorandom number generator.
        If the entropy pool runs out, previously released entropy will be used.
        If blocking is unnacceptable, use this over "dev_urandom_entropy".
    """
    return os.urandom(numbytes)


def dev_random_entropy(numbytes, fallback_to_urandom=True, timeout=5.0):
    """ Reads random bytes from the /dev/random entropy pool.

        NOTE: /dev/random is a blocking pseudorandom number generator.
        If the entropy pool runs out, this function will block until more
        environmental noise is gathered.
        If entropy re-use is unnacceptable use this over "dev_urandom_entropy".

        If "fallback_to_urandom" is set, this function will fallback to
        /dev/urandom on operating systems without /dev/random.

        If timeout is positive, this method will raise an exception if it 
        cannot read enough data from /dev/random.  If it is negative or 0,
        the method will block.
    """

    if os.name == 'nt' and fallback_to_urandom:
        return dev_urandom_entropy(numbytes)

    out_of_time = OutOfEntropyException("Insufficient entropy.  Try installing rng-tools.")

    try:
        with open("/dev/random", "rb") as f:
            # non-blocking 
            flags = fcntl.fcntl( f.fileno(), fcntl.F_GETFL )
            fcntl.fcntl( f.fileno(), fcntl.F_SETFL, flags | os.O_NONBLOCK )

            deadline = time.time() + timeout
            buf = ""

            # begin reading
            while (timeout <= 0 or time.time() < deadline) and len(buf) < numbytes:
                readable, _, _ = select.select( [f], [], [], max(timeout, 0.1) )
                if len(readable) == 0:
                    continue

                # have data
                tmpbuf = f.read(numbytes - len(buf))
                buf += tmpbuf

            if len(buf) < numbytes:
                # deadline exceeded
                raise out_of_time

            return buf

    except KeyboardInterrupt:
        raise out_of_time


def secure_randint(min_value, max_value, system_random=None):
    """ Return a random integer N such that a <= N <= b.

        Uses SystemRandom for generating random numbers.
        (which uses os.urandom(), which pulls from /dev/urandom)
    """
    if not system_random:
        system_random = random.SystemRandom()
    return system_random.randint(min_value, max_value)
