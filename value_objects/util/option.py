
from value_objects.util.decorate import wraps

class Option( object ):
  
  class Option_cannot_wrap_none( Exception ): pass
  
  class Option_cannot_wrap_option( Exception ): pass
  class Option_cannot_wrap_nothing( Option_cannot_wrap_option ): pass
  
  class Tried_to_access_nothing( Exception ): pass
  
  # ------------------------------------

  def __init__( s, inner ):
    s._validate( inner )
    s._inner = inner
  
  def _validate( s, inner ):
    try:
      nothing
    except NameError:
      return
      
    if inner is None:
      raise s.Option_cannot_wrap_none()
    
    if isinstance( inner, Option ):   
      if inner is nothing:
        raise s.Option_cannot_wrap_nothing()
      else:
        raise s.Option_cannot_wrap_option()

  # ------------------------------------

  def __str__( s ):
    if s.exists:
      return 'Option( %s )' % s._inner
    else:
      return 'nothing'

  # ------------------------------------

  def __hash__( s ):
    return hash( s._inner )
  
  def __eq__( s, other ):
    if not isinstance( other, Option ):
      return False
    
    return s._inner == other._inner

  def __ne__( s, other ):
    return not s.__eq__( other )

  # ------------------------------------
  
  @property
  def option( s ):
    if s.exists:
      return s._inner
    else:
      raise s.Tried_to_access_nothing()

  # ------------------------------------
    
  @property
  def exists( s ):
    return s._inner is not None

  # ------------------------------------

  def option_default( s, default ):
    if s.exists:
      return s.option
    else:
      return default

  # ------------------------------------

  @classmethod
  def wrap( s, x ):
    if isinstance( x, Option ):
      return x
    elif x is None:
      return nothing
    else:
      return Option( x )
    
  # ------------------------------------
  
  @classmethod
  def wrapper( s, inner ):
    
    @wraps( inner )
    def outer( *a, **kw ):
      val = inner( *a, **kw )
      return Option.wrap( val )
    
    return outer
  
# ------------------------------------------------------------------------------

nothing = Option( None )
