from distutils.core import setup

# http://guide.python-distribute.org/creation.html
setup( 
    name = 'value_objects',
    version = '2.0.1',
    author = 'Steve Wedig',
    packages = [
      'value_objects', 
      'value_objects.mixins',
      'value_objects.opt', 
      'value_objects.util',
    ],
    url = 'https://github.com/stevewedig/value-objects-in-python/',
    license = 'LICENSE.txt',
    description = 'Helpers for implementing value objects.',
    long_description = 'The online documentation can be found here: https://github.com/stevewedig/value-objects-in-python/blob/master/README.md',
 )

