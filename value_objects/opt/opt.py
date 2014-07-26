
from value_objects.util.decorate import wraps
from value_objects.mixins.value_mixin import ValueMixin

class Opt( ValueMixin ):

  class OptCannotWrapNone( Exception ): pass

  class OptCannotWrapOpt( Exception ): pass
  class OptCannotWrapAbsent( OptCannotWrapOpt ): pass

  class OptWasAbsent( Exception ): pass

  # ====================================

  def __init__( s, _item ):
    
    if s._item is None and absent_has_been_created:
      raise s.OptCannotWrapNone()

    if isinstance( s._item, Opt ):
      if s._item is Opt.absent:
        raise s.OptCannotWrapAbsent()
      else:
        raise s.OptCannotWrapOpt()

  # ====================================

  def __unicode__( s ):
    if s.is_present:
      return 'Opt( %s )' % s._item
    else:
      return 'Opt.absent'

  def __repr__( s ):
    if s.is_present:
      return 'Opt( %s )' % repr( s._item )
    else:
      return 'Opt.absent'

  # ====================================

  def __hash__( s ):
    return hash( s._item )

  def __eq__( s, other ):
    if not isinstance( other, Opt ):
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
  def Opt( s ):
    if s.is_present:
      return s._item
    else:
      raise s.OptWasAbsent()

  # ====================================

  def Opt_default( s, default ):
    if s.is_present:
      return s.Opt
    else:
      return default

  # ====================================

  @classmethod
  def adapt( s, x ):
    if isinstance( x, Opt ):
      return x
    elif x is None:
      return Opt.absent
    else:
      return Opt( x )

  @classmethod
  def adapter( s, fn ):

    @wraps( fn )
    def outer( *a, **kw ):
      output = fn( *a, **kw )
      return Opt.adapt( output )

    return outer

# ==============================================================================

absent_has_been_created = False

Opt.absent = Opt( None ) # singleton

absent_has_been_created = True
