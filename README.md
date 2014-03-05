Immutable Value Objects in Python
=======================

(This is a work in progress: the blog post isn't published.)

GitHub has a rendered version of this readme: https://github.com/stevewedig/value-objects-in-python/blob/master/README.md

* This project's GitHub repo: https://github.com/stevewedig/value-objects-in-python
* Blog post explaining this project: [Immutable Value Objects in Java & Python](http://stevewedig.com)
* This project is in the public domain via [Unlicense](http://unlicense.org).

[Vladimir Keleshev](https://github.com/halst) has an alternative Python library for [value objects](https://github.com/halst/value) that makes some slightly different design decisions. My library is a combination of techniques I've used for years and Vladimir's choice for syntax (using `__init__` to indicate field name, order, and default values).

## Project Organization

This project follows the standard distribution structure described here: http://guide.python-distribute.org/creation.html

* **Code Directory**: value_objects/
* **Test file with an example**: value_objects/testValueObjectExample.py

## Using the Library

The "value_objects" package exports 3 objects: ValueObject, frozendict, and once.

### Pip Install

The easiest way to use this library is to use [Pip](http://en.wikipedia.org/wiki/Pip_(package_manager)):

    pip install value_objects

### Copying Library Files

Alternatively you can just copy the library directory into your own codebase.

## Other Blog Posts

In addition to this project's blog post ([Immutable Value Objects in Java & Python](http://stevewedig.com)), here are others that may interest you:

* [A Software Developer's Reading List](http://stevewedig.com/2014/02/03/software-developers-reading-list/)
* [Why & How I Write Java](http://stevewedig.com/2014/02/17/why-and-how-i-write-java/)

