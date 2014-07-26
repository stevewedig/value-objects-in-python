
import unittest

from value_objects import Option
from value_objects.testing import eq, ne, raises

class OptionTestCase( unittest.TestCase ):
  
  
  def test_nothing( self ):
    
    assert not Option.absent.is_present
    
    ne( Option.absent, None )
    
    raises(
      Option.OptionWasAbsent,
      lambda: Option.absent.option
    )
    
  # ==============================================================================
  
  def test_something( self ):
  
    five = Option( 5 )
    
    assert five.is_present
    
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
  
  def test_nothing_2( self ):
    assert not Option.absent.is_present
    
    assert Option.absent != None
   
    raises(
      Option.OptionWasAbsent,
      lambda: Option.absent.option
    )
    
  # ==============================================================================
  
  def test_something_2( self ):
  
    five = Option( 5 )
    
    assert five.is_present
    
    assert 5 == five.option
    
    assert Option( 5 ) == Option( 5 )
  
    assert five != Option.absent
  
  # ==============================================================================
  
  def test_invalid_input( self ):
    raises(
      Option.OptionCannotWrapNone,
      Option,
      None
    )
    
    raises(
      Option.OptionCannotWrapAbsent,
      Option,
      Option.absent
    )
      
    raises(
      Option.OptionCannotWrapOption,
      Option,
      Option( 5 ),
    )
    
  # ==============================================================================
  
  def test_adapt( self ):
    eq(
      Option.absent,
      Option.adapt( Option.absent ),
    )
  
    eq(
      Option( 5 ),
      Option.adapt( Option( 5 ) ),
    )
    
    eq(
      Option.absent,
      Option.adapt( None ),
    )
    
    eq(
      Option( 5 ),
      Option.adapt( 5 ),
    )
  
  # ==============================================================================
  
  def test_adapter_fn( self ):
    
    @Option.adapter  
    def fn( x ):
      return x
  
    eq( Option.absent, fn( None ) )
    eq( Option( 5 ), fn( 5 ) )
    
  
  def test_adapter_method( self ):
  
    class Person( object ):
      @Option.adapter
      def method( s, x ):
        return x
    
    person = Person()
    
    eq( Option.absent, person.method( None ) )
    eq( Option( 5 ), person.method( 5 ) )

