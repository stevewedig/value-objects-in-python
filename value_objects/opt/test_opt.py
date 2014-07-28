
import unittest

from value_objects import Opt
from value_objects.util.testing import eq, ne, raises, assert_equal_objects_and_strings, assert_unequal_objects_and_strings

class OptTestCase( unittest.TestCase ):

  def test_opt_is_value( self ):

    assert_equal_objects_and_strings( 
      Opt( 1 ),
      Opt( 1 ),
    )

    assert_unequal_objects_and_strings( 
      Opt( 1 ),
      Opt( 2 ),
    )

    assert_unequal_objects_and_strings( 
      Opt( 1 ),
      Opt.absent,
    )

    assert_equal_objects_and_strings( 
      Opt.absent,
      Opt.absent,
    )

  # ====================================

  def test_absent( self ):

    assert not Opt.absent.is_present
    assert Opt.absent.is_absent

    assert Opt.absent is not None

    raises( 
      Opt.OptWasAbsent,
      lambda: Opt.absent.opt
    )

    eq(
      6,
      Opt.absent.opt_default( 6 )
    )
  
  # ====================================

  def test_present( self ):

    five = Opt( 5 )

    assert five.is_present
    assert not five.is_absent

    eq( 
      5,
      five.opt
    )

    eq( 
      5,
      five.opt_default( 6 )
    )

    eq( five, Opt( 5 ) )

    ne( five, Opt.absent )

  # ====================================

  def test_invalid_input( self ):
    raises( 
      Opt.OptCannotWrapNone,
      Opt,
      None
    )

    raises( 
      Opt.OptCannotWrapAbsent,
      Opt,
      Opt.absent
    )

    raises( 
      Opt.OptCannotWrapOpt,
      Opt,
      Opt( 5 ),
    )

  # ====================================

  def test_adapt( self ):
    eq( 
      Opt.absent,
      Opt.adapt( Opt.absent ),
    )

    eq( 
      Opt( 5 ),
      Opt.adapt( Opt( 5 ) ),
    )

    eq( 
      Opt.absent,
      Opt.adapt( None ),
    )

    eq( 
      Opt( 5 ),
      Opt.adapt( 5 ),
    )

  # ====================================

  def test_adapter_fn( self ):

    @Opt.adapter
    def fn( x ):
      return x

    eq( Opt.absent, fn( None ) )
    eq( Opt( 5 ), fn( 5 ) )


  def test_adapter_method( self ):

    class Person( object ):
      @Opt.adapter
      def method( s, x ):
        return x

    person = Person()

    eq( Opt.absent, person.method( None ) )
    eq( Opt( 5 ), person.method( 5 ) )

