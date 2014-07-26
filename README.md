
(This is a work in progress: the blog post isn't published.)

Value Objects in Python
=======================

(GitHub has a rendered version of this readme: https://github.com/stevewedig/value-objects-in-python/blob/master/README.md)

This library provides helpers for implementing value objects in Python. The library's rationale and usage instructions can be found in this blog post: [Value Objects in Java & Python](http://stevewedig.com).

* **GitHub Repo**: https://github.com/stevewedig/value-objects-in-python
* **License**: This project is in the public domain via [Unlicense](http://unlicense.org).

[Vladimir Keleshev](https://github.com/halst) has an alternative Python library for [value objects](https://github.com/halst/value) that makes some slightly different design decisions. My library is a combination of techniques I've used before and Vladimir's choice for syntax (using `__init__` to indicate field name, order, and default values).

### Installation via Pip

The easiest way to use this library is to use [Pip](http://en.wikipedia.org/wiki/Pip_(package_manager)):

    pip install value_objects

### Installation via copying files

Alternatively you can just copy the library code directory into your own codebase.

## Other Blog Posts

In addition to this project's blog post ([Value Objects in Java & Python](http://stevewedig.com)), here are others that may be of interest:

* [A Software Developer's Reading List](http://stevewedig.com/2014/02/03/software-developers-reading-list/)
* [Why & How I Write Java](http://stevewedig.com/2014/02/17/why-and-how-i-write-java/)

