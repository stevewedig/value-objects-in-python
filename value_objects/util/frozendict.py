
# http://legacy.python.org/dev/peps/pep-0416/
# http://code.activestate.com/recipes/414283-frozen-dictionaries/
# https://github.com/slezica/python-frozendict

from value_objects.util.not_mutable import not_mutable
from value_objects.util.once import once


class frozendict( dict ):
  '''
  An immutable dictionary that behaves as a value
  '''

  def __eq__( self, other ):
    if not isinstance( other, frozendict ):
      return False
    
    return self.item_set == other.item_set
  
  def __ne__( self, other ):
    return not self.__eq__( other )

  def __hash__( self ):
    return hash( self.item_set )

  @once
  def item_set( self ):
    try:
      items = self.iteritems()
    except AttributeError:
      items = self.items()

    return frozenset( items )

  __delitem__ = not_mutable
  __setitem__ = not_mutable
  clear = not_mutable
  pop = not_mutable
  popitem = not_mutable
  setdefault = not_mutable
  update = not_mutable

  def __repr__( self ):
    return "frozendict(%s)" % dict.__repr__( self )

