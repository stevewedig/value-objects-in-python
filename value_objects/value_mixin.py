
# https://github.com/nschloe/matplotlib2tikz/issues/20
try:
    # Python 2
    from itertools import izip
except ImportError:
    # Python 3
    izip = zip

from inspect import getargspec

from once import once
from object_mixin import ObjectMixin

# ==============================================================================

class ObjectHelper( object ):
  
  def __init__( self, object_class, field_names, field_values ):
    self.object_class = object_class
    self.field_names = field_names
    self.field_values = field_values

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

  def class_and_state_equals( self, other_object ):
    try:
      other_helper = other_object.object_helper
    except AttributeError:
      return False
  
    return self.class_and_state == other_helper.class_and_state
  
  @once
  def class_and_state_hash( self ):
    return hash( self.class_and_state )

  @property
  def field_pairs( self ):
    return izip( self.field_names, self.field_values )

  @once
  def class_and_state( self ):
    return ( self.object_class, self.field_values )
    
# ==============================================================================
# ValueMixin
# ==============================================================================

class ValueMixin( ObjectMixin ):

  def __new__( klass, *positionalFields, **keywordFields ):

    # Could use a metaclass to do this during class construction instead of
    # during instance construction, but I don't want to get into that.
    initClass( klass )

    instance = object.__new__( klass )

    instance.__dict__.update( izip( klass.fieldNames, positionalFields ) )
    instance.__dict__.update( keywordFields )

    return instance

  # ====================================
  # fields
  # ====================================

  @once
  def fieldValues( self ):
    return tuple( getattr( self, name ) for name in self.fieldNames )

  @property
  def fieldPairs( self ):
    return izip( self.fieldNames, self.fieldValues )

  @once
  def object_helper( self ):
    return ObjectHelper(
      object_class = type( self ), 
      field_names = self.fieldNames, 
      field_values = self.fieldValues,
    )

  # ====================================
  # str and repr
  # ====================================

  def __repr__( self ):
    return self.object_helper.class_and_state_repr

  def __unicode__( self ):
    return self.object_helper.class_and_state_unicode

  # ====================================
  # hash
  # ====================================

  def __hash__( self ):
    return self.object_helper.class_and_state_hash

  # ====================================
  # equals
  # ====================================

  def __eq__( self, other ):
    return self.object_helper.class_and_state_equals( other )

  def __ne__( self, other ):
    return not self.__eq__( other )

# ==============================================================================
# helpers
# ==============================================================================

def initClass( klass ):

  # only need to init class once
  # checking .valueObjectClass enables init to happen for subclasses
  try:
    if klass == klass.valueObjectClass:
      return
  except:
    pass

  setattr( klass, 'valueObjectClass', klass )

  fieldNames, defaultValues = parseFieldNamesAndDefaultValues( klass.__init__ )
  setattr( klass, 'fieldNames', fieldNames )

  # defaultValues implemented as class attributes
  for name, defaultValue in izip( reversed( fieldNames ), reversed( defaultValues ) ):
    setattr( klass, name, defaultValue )

def parseFieldNamesAndDefaultValues( init ):

  fieldNames, args, kwargs, defaultValues = getargspec( init )

  # remove self
  fieldNames = tuple( fieldNames[1:] )

  if args:
      raise ValueError( 'ValueMixin: `*args` are not allowed in __init__' )

  if kwargs:
      raise ValueError( 'ValueMixin: `**kwargs` are not allowed in __init__' )

  if not all( type( name ) is str for name in fieldNames ):
      raise ValueError( 'ValueMixin: parameter unpacking is not allowed in __init__' )

  defaultValues = () if not defaultValues else defaultValues

  return fieldNames, defaultValues


