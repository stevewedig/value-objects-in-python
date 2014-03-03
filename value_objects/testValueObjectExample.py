
from __init__ import ValueObject, frozendict

import unittest

# class PathQuery(ValueObject):
#   def __init__( self, path, query ):
#     pass

# ==============================================================================
# Path, Query, PathQuery
# ==============================================================================

class Path( ValueObject ):
  def __init__( self, parts ):
    pass

class Query( ValueObject ):
  def __init__( self, key__val ):
    pass

class PathQuery( ValueObject ):
  def __init__( self, path, query ):
    pass

# ==============================================================================
# test
# ==============================================================================

LOOK_AT_PRINTING = False

class ValueObjectTestCase( unittest.TestCase ):

  def testValueObjectExample( self ):
    # 3 paths
    path1 = Path(('blog', 'posts'))
    path2 = Path(('blog', 'posts'))
    path3 = Path(('blog', 'comments'))

    # path 1 and 2 are different instances, but have same value
    assert path1 is not path2
    assert path1 == path2
    assert hash(path1) == hash(path2)
    assert repr(path1) == repr(path2)
    assert str(path1) == str(path2)

    # path 1 and 3 have different value
    assert path1 != path3
    assert hash(path1) != hash(path3)
    assert repr(path1) != repr(path3)
    assert str(path1) != str(path3)
    
    # 1 query
    query = Query(frozendict(id='1'));

    # 3 path queries
    pathQuery1 = PathQuery(path1, query);
    pathQuery2 = PathQuery(path2, query);
    pathQuery3 = PathQuery(path3, query);
 
    # pathQuery 1 and 2 are different instances, but have same value
    assert pathQuery1 is not pathQuery2
    assert pathQuery1 == pathQuery2
    assert hash(pathQuery1) == hash(pathQuery2)
    assert repr(pathQuery1) == repr(pathQuery2)
    assert str(pathQuery1) == str(pathQuery2)
 
    # pathQuery 1 and 3 have different value
    assert pathQuery1 != pathQuery3
    assert hash(pathQuery1) != hash(pathQuery3)
    assert repr(pathQuery1) != repr(pathQuery3)
    assert str(pathQuery1) != str(pathQuery3)
    
    # look at printing
    if LOOK_AT_PRINTING: 
      print "printing value objects..."
      print path1
      print query
      print pathQuery1
      
      raise Exception("Check console to see what value object's toString() looks like")

