
# ==============================================================================
# once
#
# http://stevewedig.com/2014/01/27/a-few-python-tricks/
# ==============================================================================

def once( compute ):
  '''
  Use @once instead of @property when you want a cached property 
  '''
    
  # global count ensures uniqueness even when the function is unnamed (i.e. lambda)
  global once_count
  once_count += 1
  
  # including __name__ for debugging convenience
  key = '__once%s__%s' % ( once_count, compute.__name__ )

  @property  
  @wraps( compute )
  def cached_compute( s ):
    if not hasattr( s, key ):
      val = compute( s )
      setattr( s, key, val )
      
    return getattr( s, key )

  return cached_compute

once_count = 0

# ==============================================================================
# http://wiki.python.org/moin/PythonDecoratorLibrary
# ==============================================================================

def wraps( inner ):
  def wrapper( outer ):
    copy_fn_meta( src = inner, dst = outer )
    return outer
  return wrapper

def copy_fn_meta( src, dst ):
  dst.__name__ = src.__name__
  dst.__doc__ = src.__doc__
  dst.__dict__.update( src.__dict__ )

