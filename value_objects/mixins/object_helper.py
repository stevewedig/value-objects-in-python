
from value_objects.util.compat import izip, unicode
from value_objects.util.once import once

class ObjectHelper( object ):

  def __init__( self, object_class, field_names, field_values ):
    self.object_class = object_class
    self.field_names = field_names
    self.field_values = field_values

  @property
  def field_pairs( self ):
    return izip( self.field_names, self.field_values )

  @once
  def class_and_state( self ):
    return ( self.object_class, self.field_values )

  # ====================================
  # strs
  # ====================================

  @once
  def class_and_state_unicode( self ):

    pairStrs = ( 
      '%s=%s' % ( name, unicode( value ) ) for name, value in self.field_pairs
    )

    body = ', '.join( pairStrs )

    return '%s{%s}' % ( self.object_class.__name__, body )

  @once
  def class_and_state_repr( self ):

    pairStrs = ( 
      '%s=%s' % ( name, repr( value ) ) for name, value in self.field_pairs
    )

    body = ', '.join( pairStrs )

    return '%s{%s}' % ( self.object_class.__name__, body )

  # ====================================
  # equals
  # ====================================

  def class_and_state_equals( self, other_object ):
    try:
      other_helper = other_object.object_helper
    except AttributeError:
      return False

    if not isinstance( other_helper, ObjectHelper ):
      return False

    return self.class_and_state == other_helper.class_and_state

  # ====================================
  # hash
  # ====================================

  @once
  def class_and_state_hash( self ):
    return hash( self.class_and_state )


