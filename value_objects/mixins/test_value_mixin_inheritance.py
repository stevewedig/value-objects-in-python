
import unittest

from value_objects import ValueMixin
from value_objects.util.testing import eq, raises

# ============================================================================
# classes
# ============================================================================

class Parent( ValueMixin ):
  def __init__( self, a, c = 9 ):
    pass

  @property
  def double_a( self ):
    return self.a * 2

class Child( Parent ):
  def __init__( self, a, b, c = 99 ):  # these field_names should be a superset
    pass

  @property
  def triple_b( self ):
    return self.b * 3


# ============================================================================
# make sure inheritance works (not that I really ever use it)
# ============================================================================

class ValueMixinInheritanceTestCase( unittest.TestCase ):

  def test_value_mixin_inheritance( self ):

    parent = Parent( 1 )
    eq( 1, parent.a )
    eq( 2, parent.double_a )
    eq( 9, parent.c )

    parent = Parent( 1, c = 64325 )
    eq( 1, parent.a )
    eq( 2, parent.double_a )
    eq( 64325, parent.c )

    raises( 
      TypeError,
      lambda: Parent( 1, 2, 3 ),
    )

    child = Child( 1, 10 )
    eq( 1, child.a )
    eq( 2, child.double_a )
    eq( 10, child.b )
    eq( 30, child.triple_b )
    eq( 99, child.c )

    child = Child( 1, 10, c = 4562 )
    eq( 1, child.a )
    eq( 2, child.double_a )
    eq( 10, child.b )
    eq( 30, child.triple_b )
    eq( 4562, child.c )

    # internal details
    eq( ( 'a', 'c' ), parent.field_names )
    eq( ( 'a', 'b', 'c' ), child.field_names )

