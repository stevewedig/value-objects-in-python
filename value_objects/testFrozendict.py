
import unittest

from tdd import eq, ne, raises
from frozendict import frozendict

class FrozendictTestCase( unittest.TestCase ):

  def testIdentity( self ):
    dict_0 = frozendict()

    dict_1 = frozendict( 
      x = 1,
      y = frozendict( 
        z = 2,
      ),
    )

    dict_2 = frozendict( 
      y = frozendict( 
        z = 2,
      ),
      x = 1,
    )

    assert dict_0 is not dict_2
    assert dict_1 is not dict_2

    ne( dict_0, dict_1 )
    eq( dict_1, dict_2 )

    ne( 
      hash( dict_0 ),
      hash( dict_1 ),
    )

    eq( 
      hash( dict_1 ),
      hash( dict_2 ),
    )

    verify_dict = {
      dict_1 : 'verify'
    }
    assert dict_0 not in verify_dict
    eq( 'verify', verify_dict[ dict_1 ] )
    eq( 'verify', verify_dict[ dict_2 ] )

    verify_set = set( [ dict_1, dict_2 ] )

    eq( 1, len( verify_set ) )
    assert dict_0 not in verify_set
    assert dict_1 in verify_set
    assert dict_2 in verify_set

    verify_set.add( dict_0 )
    eq( 2, len( verify_set ) )

  def testImmutable( self ):
    d = frozendict( { 1 : 1 } )

    def update():
      d.update( {} )

    def setitem():
      d[ 1 ] = 2

    def pop():
      d.pop()

    def popitem():
      d.popitem()

    fns = [
      lambda: d.update( {} ),
      lambda: d.__setitem__( 1, 2 ),
      lambda: d.__delitem__( 1 ),
      lambda: d.setdefault( 1, 2 ),
      lambda: d.pop(),
      lambda: d.popitem(),
      lambda: d.clear(),
    ]

    for fn in fns:
      raises( AttributeError, fn )

