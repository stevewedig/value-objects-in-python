
import sys
from inspect import getargspec

from value_objects.util.compat import izip
from value_objects.mixins.object_helper import ObjectHelper

# ==============================================================================

class ObjectMixin( object ):

  def __new__( klass, *positional_fields, **keyword_fields ):

    # Could use a metaclass to do this during class construction instead of
    # during instance construction, but I don't want to get into that.
    initialize_class( klass )

    instance = object.__new__( klass )

    instance.__dict__.update( izip( klass.field_names, positional_fields ) )
    instance.__dict__.update( keyword_fields )

    return instance

  # ====================================
  # creating object_helper
  # ====================================

  # self.is_entity is an abstract hook, set by ValueMixin or EntityMixin

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

    field_values = tuple( getattr( self, name ) for name in self.field_names )

    return ObjectHelper( 
      object_class = type( self ),
      field_names = self.field_names,
      field_values = field_values,
    )

  # ====================================
  # delegating to object_helper
  # ====================================

  # http://stackoverflow.com/questions/1307014/python-str-versus-unicode
  if sys.version_info[0] >= 3:  # Python 3
      def __str__( self ):
          return self.__unicode__()
  else:  # Python 2
      def __str__( self ):
          return self.__unicode__().encode( 'utf8' )

  def __repr__( self ):
    return self.object_helper.class_and_state_repr

  def __unicode__( self ):
    return self.object_helper.class_and_state_unicode

  # ValueMixin also delegates __eq__() and __hash__()

# ==============================================================================
# helpers
# ==============================================================================

def initialize_class( klass ):

  # only need to the initialize_class once
  # checking .class_that_was_initialzed enables initialize_class to happen for subclasses
  # (see test_value_mixin_inheritance.py)
  try:
    if klass == klass.class_that_was_initialzed:
      return
  except:
    pass

  klass.class_that_was_initialzed = klass

  field_names, default_values = parse_fields( klass.__init__ )
  klass.field_names = field_names

  # default_values implemented as class attributes
  for name, default_value in izip( reversed( field_names ), reversed( default_values ) ):
    setattr( klass, name, default_value )

def parse_fields( init ):

  field_names, args, kwargs, default_values = getargspec( init )

  # remove self
  field_names = tuple( field_names[1:] )

  if args:
      raise ValueError( '`*args` are not allowed in __init__' )

  if kwargs:
      raise ValueError( '`**kwargs` are not allowed in __init__' )

  if not all( type( name ) is str for name in field_names ):
      raise ValueError( 'parameter unpacking is not allowed in __init__' )

  default_values = () if not default_values else default_values

  return field_names, default_values

