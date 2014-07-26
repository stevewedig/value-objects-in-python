
# http://wiki.python.org/moin/PythonDecoratorLibrary

def wraps( inner ):
  def wrapper( outer ):
    copy_fn_meta( src = inner, dst = outer )
    return outer
  return wrapper

def copy_fn_meta( src, dst ):
  dst.__name__ = src.__name__
  dst.__doc__ = src.__doc__
  dst.__dict__.update( src.__dict__ )

