
import unittest

from value_objects import Option
from value_objects.util.testing import eq, ne, raises, assert_equal_objects_and_strings, assert_unequal_objects_and_strings

class OptionTestCase( unittest.TestCase ):

  def test_option_is_value( self ):

    assert_equal_objects_and_strings( 
      Option( 1 ),
      Option( 1 ),
    )

    assert_unequal_objects_and_strings( 
      Option( 1 ),
      Option( 2 ),
    )

    assert_unequal_objects_and_strings( 
      Option( 1 ),
      Option.absent,
    )

    assert_equal_objects_and_strings( 
      Option.absent,
      Option.absent,
    )

  # ====================================

  def test_absent( self ):

    assert not Option.absent.is_present
    assert Option.absent.is_absent

    assert Option.absent is not None

    raises( 
      Option.OptionWasAbsent,
      lambda: Option.absent.option
    )

  # ====================================

  def test_present( self ):

    five = Option( 5 )

    assert five.is_present
    assert not five.is_absent

    eq( 
      5,
      five.option
    )

    eq( five, Option( 5 ) )

    ne( five, Option.absent )

  # ====================================

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

  # ====================================

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

  # ====================================

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

