
import unittest

from value_objects.util.tdd import eq, ne, raises
from value_objects.util.option import Option, nothing

# ==============================================================================
# ==============================================================================

class OptionTestCase( unittest.TestCase ):
  
  
  def test_nothing( self ):
    
    assert not nothing.exists
    
    ne( nothing, None )
    
    raises(
      Option.Tried_to_access_nothing,
      lambda: nothing.option
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
    
    ne( five, nothing )
  
  # ==============================================================================
  # ==============================================================================
  
  def test_nothing_2( self ):
    assert not nothing.exists
    
    assert nothing != None
   
    raises(
      Option.Tried_to_access_nothing,
      lambda: nothing.option
    )
    
  # ==============================================================================
  # ==============================================================================
  
  def test_something_2( self ):
  
    five = Option( 5 )
    
    assert five.exists
    
    assert 5 == five.option
    
    assert Option( 5 ) == Option( 5 )
  
    assert five != nothing
  
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
      nothing
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
      nothing,
      Option.wrap( nothing ),
    )
  
    eq(
      Option( 5 ),
      Option.wrap( Option( 5 ) ),
    )
    
    eq(
      nothing,
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
  
    eq( nothing, fn( None ) )
    eq( Option( 5 ), fn( 5 ) )
    
  
  def test_wrapper_method( self ):
  
    class Person( object ):
      @Option.wrapper
      def method( s, x ):
        return x
    
    person = Person()
    
    eq( nothing, person.method( None ) )
    eq( Option( 5 ), person.method( 5 ) )

