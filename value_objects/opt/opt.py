
from value_objects.util.decorate import wraps
from value_objects.mixins.value_mixin import ValueMixin

class Opt( ValueMixin ):

  class OptCannotWrapNone( Exception ): pass

  class OptCannotWrapOpt( Exception ): pass
  class OptCannotWrapAbsent( OptCannotWrapOpt ): pass

  class OptWasAbsent( Exception ): pass

  # ====================================

  def __init__( self, _item ):
    
    if self._item is None and absent_has_been_created:
      raise self.OptCannotWrapNone()

    if isinstance( self._item, Opt ):
      if self._item is Opt.absent:
        raise self.OptCannotWrapAbsent()
      else:
        raise self.OptCannotWrapOpt()

  # ====================================

  def __unicode__( self ):
    if self.is_present:
      return 'Opt( %s )' % self._item
    else:
      return 'Opt.absent'

  def __repr__( self ):
    if self.is_present:
      return 'Opt( %s )' % repr( self._item )
    else:
      return 'Opt.absent'

  # ====================================

  @property
  def is_present( self ):
    return not self.is_absent

  @property
  def is_absent( self ):
    return self._item is None

  # ====================================

  @property
  def opt( self ):
    if self.is_present:
      return self._item
    else:
      raise self.OptWasAbsent()

  # ====================================

  def opt_default( self, default ):
    if self.is_present:
      return self.opt
    else:
      return default

  # ====================================

  @classmethod
  def adapt( self, x ):
    if isinstance( x, Opt ):
      return x
    elif x is None:
      return Opt.absent
    else:
      return Opt( x )

  @classmethod
  def adapter( self, fn ):

    @wraps( fn )
    def outer( *a, **kw ):
      output = fn( *a, **kw )
      return Opt.adapt( output )

    return outer

# ==============================================================================

absent_has_been_created = False

Opt.absent = Opt( None ) # singleton

absent_has_been_created = True
