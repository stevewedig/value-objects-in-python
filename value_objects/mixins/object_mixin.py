
class ObjectMixin( object ):

  # http://stackoverflow.com/questions/1307014/python-str-versus-unicode
  def __str__( self ):
    return unicode( self ).encode( 'utf-8' )

