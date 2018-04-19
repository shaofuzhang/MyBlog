---
title: Python ORM 之 Peewee
date: 2018-04-18 23:03:49
tags: 写作 
categories: Python
---

## 前言

Peewee是python下一个轻量级的ORM框架，支持SQLite,MySQL,Postgresql,而且有很多好用的扩展。这次主要讨论的是其下的RetryOperationalError。

## 消失的 RetryOperationalError

经常遇到有使用者问，我在什么CSDN、什么知乎看到 ``` from playhouse.shortcuts import RetryOperationalError```,可我引用乃至看源码的时候并没看到这个呢？

Peewee 3.0就把RetryOperationalError移除了。

一起看看作者怎么说的：
```
The code should work with a few modifications...the signature for execute_sql() is slightly different. exception_wrapper is now __exception_wrapper__. get_cursor() is just cursor()...

You'll have to experiment, but look at the way execute_sql() is implemented and I'm sure you can sort it out.
```
大意为，execute_sql()函数有了许多变化，比如exception_wrapper调整成了现在的__exception_wrapper__，get_cursor() 调整成了cursor()。你们可以自己参看新的execute_sql去实现。
```
Removed as I have no intention of continuing to maintain it...also, it's my opinion that it's a gross hack.
```
大意为，我不想继续维护这块内容，就把它移除了，而且我认为它是个投机取巧的写法。

O(∩_∩)O哈哈~，英语都还给老师了，大致理解下。

## RetryOperationalError 实现了什么

看下源码：
```
class RetryOperationalError(object):
    def execute_sql(self, sql, params=None, require_commit=True):
        try:
            cursor = super(RetryOperationalError, self).execute_sql(
                sql, params, require_commit)
        except OperationalError:
            if not self.is_closed():
                self.close()
            with self.exception_wrapper():
                cursor = self.get_cursor()
                cursor.execute(sql, params or ())
                if require_commit and self.get_autocommit():
                    self.commit()
        return cursor
#super 执行的execute_sql函数。
    def execute_sql(self, sql, params=None, require_commit=True):
        logger.debug((sql, params))
        with self.exception_wrapper():
            cursor = self.get_cursor()
            try:
                cursor.execute(sql, params or ())
            except Exception:
                if self.get_autocommit() and self.autorollback:
                    self.rollback()
                raise
            else:
                if require_commit and self.get_autocommit():
                    self.commit()
        return cursor
```
分析下上面的代码：
首先定义了一个 RetryOperationalError 类，类定义了一个execute_sql函数，该函数先去执行继承来的execute_sql函数，如果报错，先关闭当前连接，拿到新的cursor，之后仿照super的execute_Sql执行一次cursor.execute.

了解到源码之后，我们就可以很方便的自己写一个类似的功能了。
```
from peewee import MySQLDatabase
from peewee import OperationalError


class RetryOperationalError(object):

    def execute_sql(self, sql, params=None, commit=True):
        try:
            cursor = super(RetryOperationalError, self).execute_sql(
                sql, params, commit)
        except OperationalError:
            if not self.is_closed():
                self.close()
            with __exception_wrapper__:
                cursor = self.cursor(commit)
                cursor.execute(sql, params or ())
                if commit and not self.in_transaction():
                    self.commit()
        return cursor


class MyRetryDB(RetryOperationalError, MySQLDatabase):
    pass
```

于是，用了新版Peewee同学，又想要重试复执行功能的，可以自己实现了。