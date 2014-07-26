
#  helpers for writing tests

def raises( Expected, fn, *a, **kw ):
  
  if not issubclass( Expected, Exception ):
    m = 'in raises: Expected was not a type of Exception, got %s' % ( Expected, ) 
    raise Exception( m )
  
  try:
    fn( *a, **kw )
  except Expected:
    return
 
  m = 'fn did not raise an error, expected %s' %  Expected
  raise ExceptionNotRaised( m )

class ExceptionNotRaised( AssertionError ): pass

# ==============================================================================

def eq( x, y ):
  if x != y:
    m = 'eq failed, \n%s\n\n!=\n\n%s' % ( x, y )
    raise AssertionError( m )

def ne( x, y ):
  assert x != y, 'ne( %s, %s ) failed' % ( x, y )
  
# ==============================================================================

def gt( x, y ):
  assert x > y, 'gt( %s, %s ) failed' % ( x, y )
  
def gte( x, y ):
  assert x >= y, 'gte( %s, %s ) failed' % ( x, y )
  
def lt( x, y ):
  assert x < y, 'lt( %s, %s ) failed' % ( x, y )
  
def lte( x, y ):
  assert x <= y, 'lte( %s, %s ) failed' % ( x, y )

def not_gt( x, y ):
  assert not ( x > y ), 'not_gt( %s, %s ) failed' % ( x, y )
  
def not_gte( x, y ):
  assert not ( x >= y ), 'not_gte( %s, %s ) failed' % ( x, y )
  
def not_lt( x, y ):
  assert not ( x < y ), 'not_lt( %s, %s ) failed' % ( x, y )
  
def not_lte( x, y ):
  assert not ( x <= y ), 'not_lte( %s, %s ) failed' % ( x, y )

# ==============================================================================

def assert_equal_objects_and_strings( a, b ):

  eq( a, b )
  eq( hash( a ), hash( b ) )

  eq( str( a ), str( b ) )

def assert_unequal_objects_and_strings( a, b ):

  ne( a, b )
  ne( hash( a ), hash( b ) )

  ne( str( a ), str( b ) )

def assert_unequal_objects_but_equal_strings( a, b ):

  ne( a, b )
  ne( hash( a ), hash( b ) )

  eq( str( a ), str( b ) )
