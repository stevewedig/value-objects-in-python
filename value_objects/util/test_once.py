
import unittest

from value_objects import once
from value_objects.util.testing import eq

class OnceTestCase( unittest.TestCase ):

  def test_once_example( self ):
    '''
    make sure properties decorated with @once are only computed once
    '''
    
    class Person( object ):
      def __init__( s, age ):
        s.compute_count = 0
        s.age = age

      @once
      def double_age( s ):
        s.compute_count += 1
        return s.age * 2

    person = Person( age = 5 )

    eq( 5, person.age )
    eq( 0, person.compute_count )

    eq( 10, person.double_age )
    eq( 1, person.compute_count )

    eq( 10, person.double_age )
    eq( 1, person.compute_count )

  def test_unnamed_lambdas( sef ):
    '''
    make sure lambda with the same __name__ are cached separately
    '''

    class C( object ):
      x = once( lambda s: 'x' )
      y = once( lambda s: 'y' )

    obj = C()

    eq( obj.x, 'x' )
    eq( obj.y, 'y' )

    eq( obj.x, 'x' )
    eq( obj.y, 'y' )

