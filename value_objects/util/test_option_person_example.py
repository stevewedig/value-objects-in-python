
import unittest

from value_objects.util.tdd import eq, ne, raises
from value_objects.util.once import once
from value_objects.util.option import Option, nothing

# ==============================================================================
# ==============================================================================

class Person( object ):
  def __init__(
    s,
    first_name,
    last_name,
    middle_name = None,
    social_security = None
  ):
    
    s.first_name = first_name
    s.last_name = last_name
    s._middle_name = middle_name
    s._social_security = social_security
    
  # manual
  @once
  def middle_name( s ):
    if s._middle_name is None:
      return nothing
    else:
      return Option( s._middle_name ) 
  
  # decorator
  @once
  @Option.wrapper
  def social_security( s ):
    return s._social_security
    
# ==============================================================================

class OptionTestCase( unittest.TestCase ):
  
  def test_person_example( self ):
    steve = Person(
      first_name = 'Steve',
      last_name = 'Wedig',
      middle_name = 'Michael',
      social_security = 1234,
    )
  
    assert steve.middle_name.exists
    eq( 'Michael', steve.middle_name.option )
    
    assert steve.social_security.exists
    eq( 1234, steve.social_security.option )
    
    dan = Person(
      first_name = 'Dan',
      last_name = 'Soudek',
    )
  
    assert not dan.middle_name.exists
    assert not dan.social_security.exists
  
