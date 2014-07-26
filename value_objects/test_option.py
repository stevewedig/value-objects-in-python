
import unittest

from value_objects import Option
from value_objects.testing import eq, ne, raises

# ==============================================================================
# ==============================================================================

class OptionTestCase( unittest.TestCase ):
  
  
  def test_nothing( self ):
    
    assert not Option.absent.exists
    
    ne( Option.absent, None )
    
    raises(
      Option.Tried_to_access_nothing,
      lambda: Option.absent.option
    )
    
  # ==============================================================================
  # ==============================================================================
  
  def test_something( self ):
  
    five = Option( 5 )
    
    assert five.exists
    
    eq( 
      5,
      five.option
    )
  
    assert Option( 5 ) == Option( 5 )
  
    eq(
      hash( five ),
      hash( Option( 5 ) ), 
    )
  
    eq( five, Option( 5 ) )
    
    ne( five, Option.absent )
  
  # ==============================================================================
  # ==============================================================================
  
  def test_nothing_2( self ):
    assert not Option.absent.exists
    
    assert Option.absent != None
   
    raises(
      Option.Tried_to_access_nothing,
      lambda: Option.absent.option
    )
    
  # ==============================================================================
  # ==============================================================================
  
  def test_something_2( self ):
  
    five = Option( 5 )
    
    assert five.exists
    
    assert 5 == five.option
    
    assert Option( 5 ) == Option( 5 )
  
    assert five != Option.absent
  
  # ==============================================================================
  # ==============================================================================
  
  def test_invalid_input( self ):
    raises(
      Option.Option_cannot_wrap_none,
      Option,
      None
    )
    
    raises(
      Option.Option_cannot_wrap_nothing,
      Option,
      Option.absent
    )
      
    raises(
      Option.Option_cannot_wrap_option,
      Option,
      Option( 5 ),
    )
    
  # ==============================================================================
  # ==============================================================================
  
  def test_wrap( self ):
    eq(
      Option.absent,
      Option.wrap( Option.absent ),
    )
  
    eq(
      Option( 5 ),
      Option.wrap( Option( 5 ) ),
    )
    
    eq(
      Option.absent,
      Option.wrap( None ),
    )
    
    eq(
      Option( 5 ),
      Option.wrap( 5 ),
    )
  
  # ==============================================================================
  # ==============================================================================
  
  def test_wrapper_fn( self ):
    
    @Option.wrapper  
    def fn( x ):
      return x
  
    eq( Option.absent, fn( None ) )
    eq( Option( 5 ), fn( 5 ) )
    
  
  def test_wrapper_method( self ):
  
    class Person( object ):
      @Option.wrapper
      def method( s, x ):
        return x
    
    person = Person()
    
    eq( Option.absent, person.method( None ) )
    eq( Option( 5 ), person.method( 5 ) )

