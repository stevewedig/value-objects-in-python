
# https://github.com/nschloe/matplotlib2tikz/issues/20
try:
    # Python 2
    from itertools import izip
except ImportError:
    # Python 3
    izip = zip

from inspect import getargspec

from frozendict import frozendict
from once import once
from object_mixin import ObjectMixin

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

  # ====================================
  # str and repr
  # ====================================

  def __repr__( self ):
    
    pairStrs = (
      '%s=%s' % ( name, repr( value ) ) for name, value in self.fieldPairs
    )
    
    body = ', '.join( pairStrs )
    
    return '%s{%s}' % ( self.__class__.__name__, body )

  def __unicode__( self ):
    
    pairStrs = (
      '%s=%s' % ( name, unicode( value ) ) for name, value in self.fieldPairs
    )
    
    body = u', '.join( pairStrs )
    
    return u'%s{%s}' % ( self.__class__.__name__, body )

  # ====================================
  # hash
  # ====================================

  def __hash__( self ):
    return self.valueObjectHash

  @once
  def valueObjectHash( self ):
    return hash( self.fieldValues )

  # ====================================
  # equals
  # ====================================

  def __eq__( self, other ):
    if( self.__class__ != other.__class__ ):
      return False

    return self.fieldValues == other.fieldValues

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


