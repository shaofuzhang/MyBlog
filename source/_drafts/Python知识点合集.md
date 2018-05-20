---
title: Python知识合集
date: 2018-03-06 13:57:49
tags: 写作 
categories: Python
---

## 继承

在 Python 2 中，对 object 的继承需要显式地写为 FrenchDeck(object)；而在 Python 3 中，
这个继承关系是默认的。

## magic methods

特殊方法的存在是为了被 Python 解释器调用的
https://docs.python.org/3/reference/datamodel.html 列出了83个特殊方法

1. 实现了__getitem__对象可迭代，即iterable

2.__contains__
迭代通常是隐式的，譬如说一个集合类型没有实现 __contains__ 方
法，那么 in 运算符就会按顺序做一次迭代搜索

3.__len__
在执行 len(my_object) 的时候，如果
my_object 是一个自定义类的对象，那么 Python 会自己去调用其中由
你实现的 __len__ 方法。
然而如果是 Python 内置的类型，比如列表（list）、字符串（str）、
字节序列（bytearray）等，那么 CPython 会抄个近路，__len__ 实际
上会直接返回 PyVarObject 里的 ob_size 属性。PyVarObject 是表示
内存中长度可变的内置对象的 C 语言结构体。直接读取这个值比调用一
个方法要快很多。

4.__iter__
，比如 for i in x: 这个语句，
背后其实用的是 iter(x)，而这个函数的背后则是 x.__iter__() 方
法。当然前提是这个方法在 x 中被实现了。

5.__repr__和__str__
__repr__ 和 __str__ 的区别在于，后者是在 str() 函数被使用，或
是在用 print 函数打印一个对象的时候才被调用的，并且它返回的字
符串对终端用户更友好。
如果你只想实现这两个特殊方法中的一个，__repr__ 是更好的选择，
因为如果一个对象没有 __str__ 函数，而 Python 又需要调用它的时
候，解释器会用 __repr__ 作为替代。

6.__bool__
默认情况下，我们自己定义的类的实例总被认为是真的，除非这个类对
__bool__ 或者 __len__ 函数有自己的实现。bool(x) 的背后是调用
x.__bool__() 的结果；如果不存在 __bool__ 方法，那么 bool(x) 会
尝试调用 x.__len__()。若返回 0，则 bool 会返回 False；否则返回
True。

## 序列

Python 标准库用 C 实现了丰富的序列类型，列举如下。
容器序列
　　list、tuple 和 collections.deque 这些序列能存放不同类型的
数据。
扁平序列
　　str、bytes、bytearray、memoryview 和 array.array，这类
序列只能容纳一种类型。
容器序列存放的是它们所包含的任意类型的对象的引用，而扁平序列
里存放的是值而不是引用。换句话说，扁平序列其实是一段连续的内存
空间。由此可见扁平序列其实更加紧凑，但是它里面只能存放诸如字
符、字节和数值这种基础类型。

序列类型还能按照能否被修改来分类。
可变序列
　　list、bytearray、array.array、collections.deque 和
memoryview。
不可变序列
　　tuple、str 和 bytes。

1.列表
列表推导不会再有变量泄漏的问题
Python 2.x 中，在列表推导中 for 关键词之后的赋值操作可能会影
响列表推导上下文中的同名变量。

```python
Python 2.7.6 (default, Mar 22 2014, 22:59:38)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 'my precious'
>>> dummy = [x for x in 'ABC']
>>> x
'C'
```

列表推导、生成器表达式，以及同它们很相似的集合（set）推导
和字典（dict）推导，在 Python 3 中都有了自己的局部作用域，就
像函数似的。表达式内部的变量和赋值只在局部起作用，表达式的
上下文里的同名变量还可以被正常引用，局部变量并不会影响到它
们。
这是Python 3 代码：

```python
>>> x = 'ABC'
>>> dummy = [ord(x) for x in x]
>>> x 
'ABC'
>>> dummy 
[65, 66, 67]
>>>
```

2.生成器
生成器表达式的语法跟列表推导差不多，只不过把方括号换成圆括号而
已。

```python
>>> a=('%s %s' % (c, s) for c in colors for s in sizes)
>>> a
<generator object <genexpr> at 0x10b1f2150>
>>> tuple(a)
('black s', 'black m', 'black l', 'white s', 'white m', 'white l')
>>> list(a)
[]
>>> a
<generator object <genexpr> at 0x10b1f2150>
>>> tuple(a)
()
>>>
```

这是因为生成器表达式背后遵守了迭代器协
议，可以逐个地产出元素，而不是先建立一个完整的列表，然后再把这
个列表传递到某个构造函数里。前面那种方式显然能够节省内存。

3.元组
除了用作不可变的列表，它还可以用于没有字段名的记录。

元组拆包形式就是平行赋值，也就是说把一个可迭代对象里
的元素，一并赋值到由对应的变量组成的元组中

```python
>>>c=a,b
# c是tuple ，即先打包成tuple
>>> a,b=c
# 在从tuple解包
```

## _和__ * 和**

#### _

_能表示前面n个变量

```python
>>> import os
>>> _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
>>> filename
'idrsa.pub'
```

#### * 

在 Python 中，函数用 *args 来获取不确定数量的参数算是一种经典写
法了。
于是 Python 3 里，这个概念被扩展到了平行赋值中，在平行赋值中，* 前缀只能用在一个变量名前面，但是这个变量可以出
现在赋值表达式的任意位置：

```python
>>> a, *body, c, d = range(5)
```




