
from decorate import wraps

class Option( object ):

  class OptionCannotWrapNone( Exception ): pass

  class OptionCannotWrapOption( Exception ): pass
  class OptionCannotWrapAbsent( OptionCannotWrapOption ): pass

  class OptionWasAbsent( Exception ): pass

  # ============================================================================

  def __init__( s, item ):
    s._validate( item )
    s._item = item

  def _validate( s, item ):

    if item is None and absent_has_been_created:
      raise s.OptionCannotWrapNone()

    if isinstance( item, Option ):
      if item is Option.absent:
        raise s.OptionCannotWrapAbsent()
      else:
        raise s.OptionCannotWrapOption()

  # ============================================================================

  # http://stackoverflow.com/questions/1307014/python-str-versus-unicode
  def __str__( self ):
    return unicode( self ).encode( 'utf-8' )

  def __unicode__( s ):
    if s.is_present:
      return 'Option( %s )' % s._item
    else:
      return 'Option.absent'

  # ============================================================================

  def __hash__( s ):
    return hash( s._item )

  def __eq__( s, other ):
    if not isinstance( other, Option ):
      return False

    return s._item == other._item

  def __ne__( s, other ):
    return not s.__eq__( other )

  # ============================================================================

  @property
  def option( s ):
    if s.is_present:
      return s._item
    else:
      raise s.OptionWasAbsent()

  # ============================================================================

  @property
  def is_present( s ):
    return not s.is_absent

  @property
  def is_absent( s ):
    return s._item is None

  # ============================================================================

  def option_default( s, default ):
    if s.is_present:
      return s.option
    else:
      return default

  # ============================================================================

  @classmethod
  def adapt( s, x ):
    if isinstance( x, Option ):
      return x
    elif x is None:
      return Option.absent
    else:
      return Option( x )

  @classmethod
  def adapter( s, fn ):

    @wraps( fn )
    def outer( *a, **kw ):
      output = fn( *a, **kw )
      return Option.adapt( output )

    return outer

# ------------------------------------------------------------------------------

absent_has_been_created = False

Option.absent = Option( None )

absent_has_been_created = True
