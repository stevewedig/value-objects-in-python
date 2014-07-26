
import unittest

from value_objects import frozendict, ValueMixin
from value_objects.util.testing import eq, ne

# ============================================================================
# Path, Query, PathQuery
# ============================================================================

class Path( ValueMixin ):
  def __init__( self, parts ):
    pass

class Query( ValueMixin ):
  def __init__( self, params ):
    pass

class PathQuery( ValueMixin ):
  def __init__( self, path, query ):
    pass

# ============================================================================
# test
# ============================================================================

class ValueMixinTestCase( unittest.TestCase ):

  def testValueMixinExample( self ):
    # 3 paths
    path1 = Path( ( 'blog', 'posts' ) )  # positional input
    path2 = Path( parts = ( 'blog', 'posts' ) )
    path3 = Path( parts = ( 'blog', 'comments' ) )

    # path 1 and 2 are different instances, but have same value
    assert path1 is not path2
    eq( path1, path2 )
    eq( hash( path1 ), hash( path2 ) )
    eq( repr( path1 ), repr( path2 ) )
    eq( str( path1 ), str( path2 ) )

    # path 1 and 3 have different value
    assert path1, path3
    ne( hash( path1 ), hash( path3 ) )
    ne( repr( path1 ), repr( path3 ) )
    ne( str( path1 ), str( path3 ) )

    # 1 query
    query = Query( frozendict( id = '1' ) )  # positional input

    # 3 path queries
    pathQuery1 = PathQuery( path1, query ) # positional input
    pathQuery2 = PathQuery( path = path2, query = query )
    pathQuery3 = PathQuery( path = path3, query = query )

    # pathQuery 1 and 2 are different instances, but have same value
    assert pathQuery1 is not pathQuery2
    eq( pathQuery1, pathQuery2 )
    eq( hash( pathQuery1 ), hash( pathQuery2 ) )
    eq( repr( pathQuery1 ), repr( pathQuery2 ) )
    eq( str( pathQuery1 ), str( pathQuery2 ) )

    # pathQuery 1 and 3 have different value
    ne( pathQuery1, pathQuery3 )
    ne( hash( pathQuery1 ), hash( pathQuery3 ) )
    ne( repr( pathQuery1 ), repr( pathQuery3 ) )
    ne( str( pathQuery1 ), str( pathQuery3 ) )

    # repr
    eq( repr(path1), "Path{parts=('blog', 'posts')}" )
    eq( repr(query), "Query{params=frozendict({'id': '1'})}" )
    eq( repr(pathQuery1), "PathQuery{path=Path{parts=('blog', 'posts')}, query=Query{params=frozendict({'id': '1'})}}" )
    
    # str (same as repr when the children have the same str as repr)
    eq( str(path1), "Path{parts=('blog', 'posts')}" )
    eq( str(query), "Query{params=frozendict({'id': '1'})}" )
    eq( str(pathQuery1), "PathQuery{path=Path{parts=('blog', 'posts')}, query=Query{params=frozendict({'id': '1'})}}" )
    
    