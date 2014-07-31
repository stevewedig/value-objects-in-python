
import unittest

from value_objects import once, Opt
from value_objects.util.testing import eq

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
      return Opt.absent
    else:
      return Opt( s._middle_name ) 
  
  # decorator
  @once
  @Opt.adapter
  def social_security( s ):
    return s._social_security
    
# ==============================================================================

class OptExampleTestCase( unittest.TestCase ):
  
  def test_person_example( self ):
    john = Person(
      first_name = 'John',
      last_name = 'Doe',
      middle_name = 'Michael',
      social_security = 1234,
    )
  
    assert john.middle_name.is_present
    assert not john.middle_name.is_absent
    eq( 'Michael', john.middle_name.opt )
    
    assert john.social_security.is_present
    assert not john.social_security.is_absent
    eq( 1234, john.social_security.opt )
    
    alice = Person(
      first_name = 'Alice',
      last_name = 'Smith',
    )
  
    assert not alice.middle_name.is_present
    assert alice.middle_name.is_absent

    assert not alice.social_security.is_present
    assert alice.social_security.is_absent
  
