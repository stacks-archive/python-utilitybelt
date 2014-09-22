Utility Belt
=============

### Charset

```python
>>> charset_to_int('deadbeef', string.hexdigits[0:16])
3735928559
>>> int_to_charset(3735928559, string.hexdigits[0:16])
'deadbeef'
>>> change_charset('deadbeef', string.hexdigits[0:16], '01')
'11011110101011011011111011101111'
>>> change_charset('11011110101011011011111011101111', '01', string.hexdigits[0:16])
'deadbeef'
```

### Dicts


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

