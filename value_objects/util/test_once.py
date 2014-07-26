
import unittest

from value_objects.util.tdd import eq
from value_objects.util.once import once

class OnceTestCase( unittest.TestCase ):

  def test_example( self ):
    
    class Person( object ):
      def __init__( s, age ):
        s.double_count = 0
        s.age = age

      @once
      def double_age( s ):
        s.double_count += 1
        return s.age * 2

    person = Person( age = 5 )

    eq( 5, person.age )
    eq( 0, person.double_count )

    eq( 10, person.double_age )
    eq( 1, person.double_count )

    eq( 10, person.double_age )
    eq( 1, person.double_count )

  def test_unnamed( sef ):
    '''
    make sure methods with the same __name__ are cached separately
    '''

    class C( object ):
      x = once( lambda s: 'x' )
      y = once( lambda s: 'y' )

    obj = C()

    eq( obj.x, 'x' )
    eq( obj.y, 'y' )

    eq( obj.x, 'x' )
    eq( obj.y, 'y' )

