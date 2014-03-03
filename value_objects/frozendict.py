
'''
from http://code.activestate.com/recipes/414283/
'''

from once import once

def blocked( *a, **kw ):
  raise AttributeError( 'A frozendict cannot be modified.' )
 
class frozendict( dict ):

  def __hash__( s ):
    return hash( s.sorted_items )

  @once
  def sorted_items( s ):
    return tuple(
        sorted(
          s.iteritems()
        )
      )
  
  __delitem__ = blocked
  __setitem__ = blocked
  clear = blocked
  pop = blocked
  popitem = blocked
  setdefault = blocked 
  update = blocked
  
  def __repr__( s ):
    return "frozendict(%s)" % dict.__repr__( s )
    
