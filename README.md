Utility Belt
=============

[![Latest Version](https://pypip.in/version/utilitybelt/badge.svg)](https://pypi.python.org/pypi/utilitybelt/)
[![Downloads](https://pypip.in/download/utilitybelt/badge.svg)](https://pypi.python.org/pypi/utilitybelt/)
[![License](https://pypip.in/license/utilitybelt/badge.svg)](https://pypi.python.org/pypi/utilitybelt>/)

### Dicts

#### Recursive dicts

```python
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
>>> scrub_dict(d)
{'a': {'b': {'c': 1}}}
```

#### Converting objects to dicts

```python
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
>>> charset_to_int('deadbeef', string.hexdigits[0:16])
3735928559
>>> int_to_charset(3735928559, string.hexdigits[0:16])
'deadbeef'
```

#### Changing arbitrary charsets

```python
>>> change_charset('deadbeef', string.hexdigits[0:16], '01')
'11011110101011011011111011101111'
>>> change_charset('11011110101011011011111011101111', '01', string.hexdigits[0:16])
'deadbeef'
```

### Numbers

```python
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

