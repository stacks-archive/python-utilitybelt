Utility Belt
=============

[![Travis](https://img.shields.io/travis/onenameio/utilitybelt.svg)](https://travis-ci.org/onenameio/utilitybelt)
[![PyPI](https://img.shields.io/pypi/v/utilitybelt.svg)](https://pypi.python.org/pypi/utilitybelt/)
[![PyPI](https://img.shields.io/pypi/dm/utilitybelt.svg)](https://pypi.python.org/pypi/utilitybelt/)
[![PyPI](https://img.shields.io/pypi/l/utilitybelt.svg)](https://github.com/onenameio/utilitybelt/blob/master/LICENSE)

### Entropy

```python
>>> from binascii import hexlify
>>> from utilitybelt import dev_random_entropy, dev_urandom_entropy
>>> hexlify(dev_random_entropy(16))
'cc8752461384261063a979bf5d92ad49'
>>> hexlify(dev_urandom_entropy(16))
'874ac235edfa658bd46c763079acc096'
```

### Base16

```python
>>> from utilitybelt import hex_to_int, int_to_hex, is_hex, is_int
>>> hex_to_int('deadbeef')
3735928559
>>> int_to_hex(3735928559)
'deadbeef'
>>> is_hex('deadbeef')
True
>>> is_hex('xdeadbeefx')
False
>>> is_int(123)
True
>>> is_int('deadbeef')
False
```

### Dicts

#### Recursive dicts

```python
>>> from utilitybelt import recursive_dict, recursive_dict_to_dict
>>> rd = recursive_dict()
>>> rd['a']['b']['c'] = 1
>>> rd['a']['b']['c']
1
>>> rd['a']['b']['d']
defaultdict(<function <lambda> at 0x102912b90>, {})
>>> d = recursive_dict_to_dict(rd); print d
{'a': {'b': {'c': 1, 'd': {}}}}
```

#### Scrubbing dicts

```python
>>> from utilitybelt import scrub_dict
>>> d
{'a': {'b': {'c': 1, 'd': {}}}}
>>> scrub_dict(d)
{'a': {'b': {'c': 1}}}
```

#### Converting objects to dicts

```python
>>> from utilitybelt import to_dict
>>> class Rectangle():
>>>     def __init__(self, width, length):
>>>         self.width = width
>>>         self.length = length
>>> rectangle = Rectangle(2, 4)
>>> to_dict(rectangle)
{'width': 2, 'length': 4}
```

### Charsets

#### Moving from string charsets to ints and vice versa

```python
>>> from utilitybelt import charset_to_int, int_to_charset
>>> charset_to_int('deadbeef', string.hexdigits[0:16])
3735928559
>>> int_to_charset(3735928559, string.hexdigits[0:16])
'deadbeef'
```

#### Changing arbitrary charsets

```python
>>> from utilitybelt import change_charset
>>> change_charset('deadbeef', string.hexdigits[0:16], '01')
'11011110101011011011111011101111'
>>> change_charset('11011110101011011011111011101111', '01', string.hexdigits[0:16])
'deadbeef'
```
