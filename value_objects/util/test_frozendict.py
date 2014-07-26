
import unittest

from value_objects import frozendict, NotMutable
from value_objects.util.testing import raises, assert_equal_objects_and_strings, assert_unequal_objects_and_strings

class FrozendictTestCase( unittest.TestCase ):

  def test_frozendict_is_value( self ):

    # ==================================
    # empty
    # ==================================

    assert_equal_objects_and_strings( 
      frozendict(),
      frozendict()
    )

    assert_unequal_objects_and_strings( 
      frozendict(),
      frozendict( a = 2 )
    )

    # ==================================
    # one key
    # ==================================

    assert_equal_objects_and_strings( 
      frozendict( a = 1 ),
      frozendict( a = 1 )
    )

    assert_unequal_objects_and_strings( 
      frozendict( a = 1 ),
      frozendict( a = 2 )
    )

    assert_unequal_objects_and_strings( 
      frozendict( a = 1 ),
      frozendict( a = 1, b = 2 )
    )

    # ==================================
    # two keys
    # ==================================

    assert_equal_objects_and_strings( 
      frozendict( 
        a = 1,
        b = 2
      ),
      frozendict( 
        b = 2,
        a = 1
      )
    )

    # ==================================
    # non str keys
    # ==================================

    assert_equal_objects_and_strings( 
      frozendict( {
        1: 2,
        3: 4,
      } ),
      frozendict( {
        1: 2,
        3: 4,
      } )
    )

    # ==================================
    # mix and match different kinds of values
    # ==================================

    assert_equal_objects_and_strings( 
      tuple( [
        'x',
        frozenset( [
          'y',
          frozendict( 
              boolean = True,
              integer = 1,
              real = 1.5,
              byte = 'byte',
              unicode = 'unicode',
          )
        ] )
      ] ),
      tuple( [
        'x',
        frozenset( [
          'y',
          frozendict( 
              boolean = True,
              integer = 1,
              real = 1.5,
              byte = 'byte',
              unicode = 'unicode',
          )
        ] )
      ] )
    )

    assert_unequal_objects_and_strings( 
      tuple( [
        'x',
        frozenset( [
          'y',
          frozendict( 
              boolean = True,
              integer = 1,
              real = 1.5,
              byte = 'byte',
              unicode = 'unicode',
          )
        ] )
      ] ),
      tuple( [
        'x',
        frozenset( [
          'y',
          frozendict( 
              boolean = False,  # only difference
              integer = 1,
              real = 1.5,
              byte = 'byte',
              unicode = 'unicode',
          )
        ] )
      ] )
    )

  # ============================================================================

  def test_immutable( self ):

    d = frozendict()

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
      raises( NotMutable, fn )

