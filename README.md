
(This is a work in progress: the blog post isn't published.)

Value Objects in Python
=======================

(GitHub has a rendered version of this readme: https://github.com/stevewedig/value-objects-in-python/)

This library makes it easy to implement value objects in Python. The library's rationale and usage instructions can be found in this blog post: [Value Objects in Java & Python](http://stevewedig.com).

* **GitHub Repo**: https://github.com/stevewedig/value-objects-in-python
* **License**: This project is in the public domain via [Unlicense](http://unlicense.org).

### Alternative library

[Vladimir Keleshev](https://github.com/halst) has an alternative Python library for [value objects](https://github.com/halst/value) that makes some different design decisions. My library is a combination of techniques I've used before and Vladimir's technique of using `__init__` to indicate field name, order, and default values.

### Installation via Pip

The easiest way to install this library is to use [Pip](http://en.wikipedia.org/wiki/Pip_(package_manager)):

    pip install value_objects

### Installation via copying files

Alternatively you can just copy the library code directory into your own codebase.

### Running Tox tests in Vagrant

[Vagrant](http://www.vagrantup.com/) (with [VirtualBox](http://en.wikipedia.org/wiki/VirtualBox) is a great way to run sandboxed experiments on your dev machine. I use Vagrant plus [Tox](https://testrun.org/tox/) to run this library's tests in Python 2.x and 3.x without affecting my dev machine. The three scripts I use are included in this project. After going through the quick Vagrant tutorial you'll be ready to try them out:

1. Setup the VM on your dev machine: [1_enter_ubuntu_vm.sh](https://github.com/stevewedig/value-objects-in-python/blob/master/vagrant/1_enter_ubuntu_vm.sh)
1. Provision and test inside the VM: [2_run_inside_ubuntu_vm.sh](https://github.com/stevewedig/value-objects-in-python/blob/master/vagrant/2_run_inside_ubuntu_vm.sh)
1. Provision: [3_provision.sh](https://github.com/stevewedig/value-objects-in-python/blob/master/vagrant/3_provision.sh)


### Other blog posts

In addition to this project's blog post ([Value Objects in Java & Python](http://stevewedig.com)), you may also be interested in these posts of mine:

* [A Software Developer's Reading List](http://stevewedig.com/2014/02/03/software-developers-reading-list/)
* [Why & How I Write Java](http://stevewedig.com/2014/02/17/why-and-how-i-write-java/)

