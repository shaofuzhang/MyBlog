---
title: Python3特性汇总
date: 2018-09-20 10:418:49
tags: 写作 
categories: Python
---

Python3.6  Print Format：f
e.x.

```python
>>> name = 'Fred'
>>> age = 42
>>> f'He said his name is {name} and he is {age} years old.'
He said his name is Fred and he is 42 years old.
```

同时可以指定 conversion
Conversion '!s' calls str() on the result, '!r' calls repr(), and '!a' calls ascii().

e.g.

```python
>>> name = "Fred"
>>> f"He said his name is {name!r}."
"He said his name is 'Fred'."
>>> f"He said his name is {repr(name)}."  # repr() is equivalent to !r
```