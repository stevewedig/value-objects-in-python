
from value_objects.mixins.object_mixin import ObjectMixin

class ValueMixin( ObjectMixin ):

  is_entity = False
  
  # ====================================
  # delegating object_helper
  # ====================================

  def __eq__( self, other ):
    return self.object_helper.class_and_state_equals( other )

  def __ne__( self, other ):
    return not self.__eq__( other )

  def __hash__( self ):
    return self.object_helper.class_and_state_hash

