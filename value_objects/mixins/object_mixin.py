
from inspect import getargspec

from value_objects.util.zip import izip

from object_helper import ObjectHelper

# ==============================================================================

class ObjectMixin( object ):

  def __new__( klass, *positionalFields, **keywordFields ):

    # Could use a metaclass to do this during class construction instead of
    # during instance construction, but I don't want to get into that.
    initClass( klass )

    instance = object.__new__( klass )

    instance.__dict__.update( izip( klass.fieldNames, positionalFields ) )
    instance.__dict__.update( keywordFields )

    return instance

  # ====================================
  # creating object_helper
  # ====================================

  # self.is_entity is an abstract hook

  @property
  def object_helper( self ):

    if self.is_entity:
      return self.uncached_object_helper

    try:
      return self.cached_object_helper
    except AttributeError:
      self.cached_object_helper = self.uncached_object_helper
      return self.cached_object_helper

  @property
  def uncached_object_helper( self ):

    field_values = tuple( getattr( self, name ) for name in self.fieldNames )

    return ObjectHelper( 
      object_class = type( self ),
      field_names = self.fieldNames,
      field_values = field_values,
    )

  # ====================================
  # delegating to object_helper
  # ====================================

  # http://stackoverflow.com/questions/1307014/python-str-versus-unicode
  def __str__( self ):
    return unicode( self ).encode( 'utf-8' )

  def __repr__( self ):
    return self.object_helper.class_and_state_repr

  def __unicode__( self ):
    return self.object_helper.class_and_state_unicode

  # ValueMixin also delegates __eq__() and __hash__()

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
