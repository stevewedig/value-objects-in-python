

from inspect import getargspec

from value_objects.util.once import once
from value_objects.util.zip import izip

from object_mixin import ObjectMixin
from object_helper import ObjectHelper

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
  # equals
  # ====================================

  def __eq__( self, other ):
    return self.object_helper.class_and_state_equals( other )

  def __ne__( self, other ):
    return not self.__eq__( other )
    
  # ====================================
  # hash
  # ====================================

  def __hash__( self ):
    return self.object_helper.class_and_state_hash

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
      raise ValueError( '`*args` are not allowed in __init__' )

  if kwargs:
      raise ValueError( '`**kwargs` are not allowed in __init__' )

  if not all( type( name ) is str for name in fieldNames ):
      raise ValueError( 'parameter unpacking is not allowed in __init__' )

  defaultValues = () if not defaultValues else defaultValues

  return fieldNames, defaultValues


