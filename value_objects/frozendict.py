
# http://stevewedig.com/2014/01/27/a-few-python-tricks/
#
# http://legacy.python.org/dev/peps/pep-0416/
# http://code.activestate.com/recipes/414283-frozen-dictionaries/
# from http://code.activestate.com/recipes/414283/
# https://github.com/slezica/python-frozendict

from once import once

def blocked( *a, **kw ):
  raise AttributeError( 'A frozendict cannot be modified.' )

class frozendict( dict ):
  '''
  An immutable and hashable dictionary
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

  __delitem__ = blocked
  __setitem__ = blocked
  clear = blocked
  pop = blocked
  popitem = blocked
  setdefault = blocked
  update = blocked

  def __repr__( s ):
    return "frozendict(%s)" % dict.__repr__( s )

