
import unittest

from value_objects import ValueMixin, EntityMixin
from value_objects.util.testing import eq, assert_equal_objects_and_strings, assert_unequal_objects_and_strings

# ============================================================================
# cache/hash test setup
# ============================================================================

class HashCounter( object ):

  def __init__( self ):
    self.hash_count = 0

  def __hash__( self ):
    self.hash_count += 1
    return 0

class ValueWithCounter( ValueMixin ):
  def __init__( self, counter ):
    pass

class EntityWithCounter( EntityMixin ):
  def __init__( self, counter ):
    pass


# ============================================================================

class MixinDetailsTestCase( unittest.TestCase ):

  def test_helper_is_cached_on_values( self ):

    value = ValueWithCounter( HashCounter() )

    # helper is cached
    assert value.object_helper is value.object_helper

    eq( 0, value.counter.hash_count )

    hash( value )
    eq( 1, value.counter.hash_count )

    # count stays at 1 forever
    hash( value )
    eq( 1, value.counter.hash_count )
    hash( value )
    eq( 1, value.counter.hash_count )

  def test_helper_not_cached_on_entities( self ):

    entity = EntityWithCounter( HashCounter() )

    # helper not cached
    assert entity.object_helper is not entity.object_helper

    eq( 0, entity.counter.hash_count )

    # nested object shouldn't be hashed
    hash( entity )
    eq( 0, entity.counter.hash_count )

  # ====================================

  def test_behavior_checking( self ):

    class A( ValueMixin ):
      def __init__( self, name ):
        pass

    class B( ValueMixin ):
      def __init__( self, name ):
        pass

    a = A( "val" )
    b = B( "val" )

    assert_unequal_objects_and_strings( a, b )

  # ====================================

  def test_default_value( self ):
    class C( ValueMixin ):
      def __init__( self, a, b = 2 ):
        pass

    o = C( 1 )

    eq( o, C( 1, 2 ) )
    eq( o.b, 2 )

  # ====================================

  def test_init_executes_after_assignment( self ):

    evaluated = [False]

    class C( ValueMixin ):
      def __init__( self, a ):

        evaluated[0] = True

        eq( self.a, 1 )

    C( 1 )

    assert evaluated[ 0 ]

  # ====================================
  
  # see the blog post for why I don't personally do this
  def test_values_can_contain_entities( self ):
    
    class C( ValueMixin ):
      def __init__( self, myFlag, myEntity ):
        pass
    
    entity_1 = object()
    entity_2 = object()
    
    assert_equal_objects_and_strings(
      C( True, entity_1 ),
      C( True, entity_1 ),
    )
    
    assert_unequal_objects_and_strings(
      C( True, entity_1 ),
      C( False, entity_1 ),
    )  
    
    assert_unequal_objects_and_strings(
      C( True, entity_1 ),
      C( True, entity_2 ),
    )  

