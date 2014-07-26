
# https://github.com/nschloe/matplotlib2tikz/issues/20
try:
    # Python 2
    from itertools import izip
except ImportError:
    # Python 3
    izip = zip
    
try:
  unicode = unicode
except NameError:
  unicode = str

