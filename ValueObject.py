
from inspect import getargspec
from itertools import izip

# ==============================================================================
# ValueObject
# ==============================================================================

class ValueObject( object ):

  def __new__( klass, *args, **kwargs ):

    initClass( klass )

    instance = object.__new__( klass, *args, **kwargs )

    instance.__dict__.update( dict( zip( klass.valueObjectFieldNames, args ) + kwargs.items() ) )

    return instance

  # ============================================================================
  # fields
  # ============================================================================

  @property
  def valueObjectFieldValues( self ):
    try:
      return self.cachedValueObjectFieldValues
    except AttributeError:
      self.cachedValueObjectFieldValues = tuple( getattr( self, name ) for name in self.valueObjectFieldNames )
      return self.cachedValueObjectFieldValues

  @property
  def valueObjectFieldCount( self ):
    return len( self.valueObjectFieldNames )

  @property
  def valueObjectFieldPairs( self ):
    return izip( self.valueObjectFieldNames, self.valueObjectFieldValues )

  # ============================================================================
  # str and repr
  # ============================================================================

  @property
  def valueObjectPairReprs( self ):
    for name, value in self.valueObjectFieldPairs:
      yield '%s=%s' % ( name, repr( value ) )

  @property
  def valueObjectPairStrs( self ):
    for name, value in self.valueObjectFieldPairs:
      yield '%s=%s' % ( name, str( value ) )

  def __repr__( self ):
    arcs = ', '.join( self.valueObjectPairReprs )
    return '%s{%s}' % ( self.__class__.__name__, arcs )

  def __str__( self ):
    arcs = ', '.join( self.valueObjectPairStrs )
    return '%s{%s}' % ( self.__class__.__name__, arcs )

  # ============================================================================
  # hash
  # ============================================================================

  def __hash__( self ):
    try:
      return self.cachedValueObjectHash
    except AttributeError:
      self.cachedValueObjectHash = hash( self.valueObjectFieldValues )
      return self.cachedValueObjectHash

  # ============================================================================
  # equals
  # ============================================================================

  def __eq__( self, other ):
    if( self.__class__ != other.__class__ ):
      return False

    return self.valueObjectFieldValues == other.valueObjectFieldValues

  def __ne__( self, other ):
    return not self.__eq__( other )

# ==============================================================================
# helpers
# ==============================================================================

def initClass( klass ):

  fieldNames, defaultValues = parseFieldNamesAndDefaultValues( klass.__init__ )

  setattr( klass, 'valueObjectFieldNames', fieldNames )

  # defaultValues implemented as class attributes
  for name, defaultValue in izip( reversed( fieldNames ), reversed( defaultValues ) ):
    setattr( klass, name, defaultValue )

def parseFieldNamesAndDefaultValues( init ):

  fieldNames, args, kwargs, defaultValues = getargspec( init )

  # remove self
  fieldNames = tuple( fieldNames[1:] )

  if args:
      raise ValueError( 'ValueObject: `*args` are not allowed in __init__' )

  if kwargs:
      raise ValueError( 'ValueObject: `**kwargs` are not allowed in __init__' )

  if not all( type( name ) is str for name in fieldNames ):
      raise ValueError( 'ValueObject: parameter unpacking is not allowed in __init__' )

  defaultValues = () if not defaultValues else defaultValues

  return fieldNames, defaultValues


