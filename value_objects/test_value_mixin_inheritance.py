
import unittest

from value_objects import ValueMixin
from value_objects.testing import eq

# ============================================================================
# AbsPath <: Path
# ============================================================================

class RelPath( ValueMixin ):
  def __init__( self, parts ):
    pass

  @property
  def dotted_path( s ):
    return '.'.join( s.parts )

class AbsPath( RelPath ):
  def __init__( self, relPath, root ):
    pass
    
  @property
  def parts( s ):
    return s.relPath.parts

# ============================================================================
# make sure inheritance works, not that I recommend it
# ============================================================================

class TestValueMixinInheritance( unittest.TestCase ):

  def testValueMixinInheritance( self ):

    relPath = RelPath( parts = ( 'blog', 'posts' ) )
    eq( relPath.dotted_path, 'blog.posts' )

    absPath = AbsPath( relPath = relPath, root = 'C:/' )

    eq( absPath.dotted_path, 'blog.posts' )
    eq( absPath.valueObjectFieldNames, ( 'relPath', 'root' ) )
    eq( repr( absPath ), "AbsPath{relPath=RelPath{parts=('blog', 'posts')}, root='C:/'}" )
