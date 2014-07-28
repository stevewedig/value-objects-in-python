
import unittest

from value_objects import EntityMixin
from value_objects.util.testing import assert_unequal_objects_but_equal_strings, assert_unequal_objects_and_strings

# ============================================================================
# Person
# ============================================================================

class Person( EntityMixin ):
  def __init__( self, name, age ):
    pass

# ============================================================================
# test
# ============================================================================

class EntityMixinTestCase( unittest.TestCase ):

  def test_entity_mixin_example( self ):
    
    bob1 = Person( name = 'bob', age = 40 )
    bob2 = Person( name = 'bob', age = 40 )
    
    # double check that we have different values but they print the same
    assert_unequal_objects_but_equal_strings( bob1, bob2 )
    
    # mutate
    bob2.age = 41
    
    # now they should't print the same
    assert_unequal_objects_and_strings( bob1, bob2 )

