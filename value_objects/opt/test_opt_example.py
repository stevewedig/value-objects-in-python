
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
    steve = Person(
      first_name = 'Steve',
      last_name = 'Wedig',
      middle_name = 'Michael',
      social_security = 1234,
    )
  
    assert steve.middle_name.is_present
    eq( 'Michael', steve.middle_name.opt )
    
    assert steve.social_security.is_present
    eq( 1234, steve.social_security.opt )
    
    dan = Person(
      first_name = 'Dan',
      last_name = 'Soudek',
    )
  
    assert not dan.middle_name.is_present
    assert not dan.social_security.is_present
  
