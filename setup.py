from distutils.core import setup

# http://guide.python-distribute.org/creation.html
setup( 
    name = 'value_objects',
    version = '0.1.0',
    author = 'Steve Wedig',
    packages = ['value_objects'],
    url = 'http://pypi.python.org/pypi/value_objects/',
    license = 'LICENSE.txt',
    description = 'Helpers for implementing immutable value objects.',
    long_description = open( 'README.md' ).read(),
 )
