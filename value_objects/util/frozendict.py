
# frozendict recipes:
# http://legacy.python.org/dev/peps/pep-0416/
# http://code.activestate.com/recipes/414283-frozen-dictionaries/
# from http://code.activestate.com/recipes/414283/
# https://github.com/slezica/python-frozendict

from value_objects.util.once import once
from value_objects.util.not_mutable import not_mutable

class frozendict( dict ):
  '''
  An immutable dictionary that behaves as a value
  '''

  def __hash__( s ):
    return hash( s.sorted_items )

  @once
  def sorted_items( s ):
    try:
      items = s.iteritems()
    except AttributeError:
      items = s.items()

    return tuple( 
      sorted( items )
    )

  __delitem__ = not_mutable
  __setitem__ = not_mutable
  clear = not_mutable
  pop = not_mutable
  popitem = not_mutable
  setdefault = not_mutable
  update = not_mutable

  def __repr__( s ):
    return "frozendict(%s)" % dict.__repr__( s )
