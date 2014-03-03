from inspect import getargspec
from itertools import izip

class ValueObject( object ):

  def __new__( klass, *args, **kwargs ):

    init = klass.__init__

    para, varargs, keywords, defaults = getargspec( init )
    if varargs:
        raise ValueError( '`*args` are not allowed in __init__' )
    if keywords:
        raise ValueError( '`**kwargs` are not allowed in __init__' )
    if not all( type( p ) is str for p in para ):
        raise ValueError( 'parameter unpacking is not allowed in __init__' )

    defaults = () if not defaults else defaults

    instance = object.__new__( klass, *args, **kwargs )

    instance.__dict__.update( dict( zip( para[:0:-1], defaults[::-1] ) ) )
    instance.__dict__.update( dict( zip( para[1:], args ) + kwargs.items() ) )

    instance.__dict__['valueObjectFieldNames'] = tuple( para[1:] )

    return instance

  # ============================================================================
  # fields
  # ============================================================================

  @property
  def valueObjectFieldValues( self ):
    return tuple( getattr( self, name ) for name in self.valueObjectFieldNames )

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

