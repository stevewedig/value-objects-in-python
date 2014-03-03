

import unittest

from tdd import raises

from __init__ import ValueObject

def fixture(init):
    class Option(ValueObject):
        __init__ = init
    return Option

class ValueObjectTestCase( unittest.TestCase ):

  def test_primitive_value(self):
      Option = fixture(lambda self: None)
      assert repr(Option()) == 'Option{}'
      assert Option() == Option()
      assert not Option() != Option()
      assert 'self' not in Option().__dict__
  
  
  def test_init_without_defaults(self):
      Option = fixture(lambda self, short, long: None)
      for option in [Option('-a', '--all'),
                     Option(short='-a', long='--all'),
                     Option('-a', long='--all')]:
          assert repr(option) == "Option{short='-a', long='--all'}"
          assert option == Option('-a', '--all')
          assert option.short == '-a'
          assert option.long == '--all'
          assert 'self' not in option.__dict__
  
          print option.valueObjectFieldNames
          print option.valueObjectFieldValues
  
  def test_init_with_defaults(self):
      Option = fixture(lambda self, short, long='--default': None)
      assert 'self' not in Option('-a').__dict__
      assert Option('-d').long == '--default'
  
  def test_corner_case_of_self_with_default(self):
      Option = fixture(lambda self='<self>', short='-a': None)
      
      print repr(Option('-a'))
      
      assert repr(Option('-a')) == "Option{short='-a'}" # modified
      assert repr(Option('-b')) == "Option{short='-b'}"
      assert 'self' not in Option('-a').__dict__


  def test_varargs_and_kwargs_are_not_allowed(self):
      Option = fixture(lambda self, *args: None)
      raises(ValueError, lambda: Option())

      Option = fixture(lambda self, **kwargs: None)
      raises(ValueError, lambda: Option())
    
  def test_tuple_parameter_unpacking_is_not_allowed(self):
      Option = fixture(lambda self, (one, two): None)
      raises(ValueError, lambda: Option())

