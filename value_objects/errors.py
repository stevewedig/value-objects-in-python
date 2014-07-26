
class NotMutable( AttributeError ):
  pass

def not_mutable( *a, **kw ):
  raise NotMutable()

