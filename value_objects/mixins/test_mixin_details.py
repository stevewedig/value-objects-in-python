
import unittest

from value_objects import ValueMixin, EntityMixin
from value_objects.util.testing import eq, assert_unequal_objects_and_strings

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