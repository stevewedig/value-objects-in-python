 
import unittest
 
from value_objects import ValueMixin
from value_objects.util.testing import eq
 
# ============================================================================
# classes
# ============================================================================
 
class RelPath( ValueMixin ):
  def __init__( self, parts ):
    pass
 
  @property
  def dotted_path( s ):
    return '.'.join( s.parts )
 
class AbsPath( RelPath ):
  def __init__( self, rel_path, root ):
    pass
     
  @property
  def parts( s ):
    return s.rel_path.parts
 
 
# ============================================================================
# make sure inheritance works, not that I recommend it
# ============================================================================
 
class TestValueMixinInheritance( unittest.TestCase ):
 
  def testValueMixinInheritance( self ):
 
    rel_path = RelPath( parts = ( 'blog', 'posts' ) )
    eq( rel_path.dotted_path, 'blog.posts' )
 
    abs_path = AbsPath( rel_path = rel_path, root = 'C:/' )
 
    eq( abs_path.dotted_path, 'blog.posts' )
    eq( abs_path.field_names, ( 'rel_path', 'root' ) )
    eq( repr( abs_path ), "AbsPath{rel_path=RelPath{parts=('blog', 'posts')}, root='C:/'}" )

