
import unittest

from .tdd import eq
from .once import once

class OnceTestCase( unittest.TestCase ):

  def testExample( self ):

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

  def testUnnamed( sef ):
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

