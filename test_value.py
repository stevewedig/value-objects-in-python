from value import Value

import unittest

def fixture(init):
    class Option(Value):
        __init__ = init
    return Option

class ValueObjectTestCase( unittest.TestCase ):

  def test_primitive_value(self):
      Option = fixture(lambda self: None)
      assert repr(Option()) == 'Option()'
      assert hash(Option()) == hash('Option()')
      assert Option() == Option()
      assert not Option() != Option()
      assert 'self' not in Option().__dict__
  
  
  def test_init_without_defaults(self):
      Option = fixture(lambda self, short, long: None)
      for option in [Option('-a', '--all'),
                     Option(short='-a', long='--all'),
                     Option('-a', long='--all')]:
          assert repr(option) == "Option('-a', '--all')"
          assert hash(option) == hash("Option('-a', '--all')")
          assert option == Option('-a', '--all')
          assert option.short == '-a'
          assert option.long == '--all'
          assert 'self' not in option.__dict__
  
  
  def test_init_with_defaults(self):
      Option = fixture(lambda self, short, long='--default': None)
      assert repr(Option('-a')) == "Option('-a')"
      assert repr(Option('-a', '--default')) == "Option('-a')"
      assert repr(Option('-a', '--all')) == "Option('-a', '--all')"
      assert 'self' not in Option('-a').__dict__
  
  
  def test_corner_case_of_self_with_default(self):
      Option = fixture(lambda self='<self>', short='-a': None)
      assert repr(Option('-a')) == "Option()"
      assert repr(Option('-b')) == "Option('-b')"
      assert 'self' not in Option('-a').__dict__


#   def test_varargs_and_kwargs_are_not_allowed(self):
#       Option = fixture(lambda self, *args: None)
#       with self.assertRaises(ValueError):
#           Option()
#       Option = fixture(lambda self, **kwargs: None)
#       with self.assertRaises(ValueError):
#           Option()
#    
#   def test_tuple_parameter_unpacking_is_not_allowed(self):
#       Option = fixture(lambda self, (one, two): None)
#       with self.assertRaises(ValueError):
#           Option()
