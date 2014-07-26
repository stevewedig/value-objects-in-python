
from value_objects.util.decorate import wraps
from value_objects.mixins.value_mixin import ValueMixin

class Option( ValueMixin ):

  class OptionCannotWrapNone( Exception ): pass

  class OptionCannotWrapOption( Exception ): pass
  class OptionCannotWrapAbsent( OptionCannotWrapOption ): pass

  class OptionWasAbsent( Exception ): pass

  # ====================================

  def __init__( s, _item ):
    
    if s._item is None and absent_has_been_created:
      raise s.OptionCannotWrapNone()

    if isinstance( s._item, Option ):
      if s._item is Option.absent:
        raise s.OptionCannotWrapAbsent()
      else:
        raise s.OptionCannotWrapOption()

  # ====================================

  def __unicode__( s ):
    if s.is_present:
      return 'Option( %s )' % s._item
    else:
      return 'Option.absent'

  def __repr__( s ):
    if s.is_present:
      return 'Option( %s )' % repr( s._item )
    else:
      return 'Option.absent'

  # ====================================

  def __hash__( s ):
    return hash( s._item )

  def __eq__( s, other ):
    if not isinstance( other, Option ):
      return False

    return s._item == other._item

  def __ne__( s, other ):
    return not s.__eq__( other )

  # ====================================

  @property
  def is_present( s ):
    return not s.is_absent

  @property
  def is_absent( s ):
    return s._item is None

  # ====================================

  @property
  def option( s ):
    if s.is_present:
      return s._item
    else:
      raise s.OptionWasAbsent()

  # ====================================

  def option_default( s, default ):
    if s.is_present:
      return s.option
    else:
      return default

  # ====================================

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

# ==============================================================================

absent_has_been_created = False

Option.absent = Option( None ) # singleton

absent_has_been_created = True
