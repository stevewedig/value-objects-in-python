
import unittest

from tdd import raises

from __init__ import ValueObject

# these tests are ported from halst's Value Object library for Python: 
# https://github.com/halst/value

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
      Option = fixture(lambda self, shortName, longName: None)
      for option in [Option('-a', '--all'),
                     Option(shortName='-a', longName='--all'),
                     Option('-a', longName='--all')]:
          assert repr(option) == "Option{shortName='-a', longName='--all'}"
          assert option == Option('-a', '--all')
          assert option.shortName == '-a'
          assert option.longName == '--all'
          assert 'self' not in option.__dict__
  
          print option.valueObjectFieldNames
          print option.valueObjectFieldValues
  
  def test_init_with_defaults(self):
      Option = fixture(lambda self, shortName, longName='--default': None)
      assert 'self' not in Option('-a').__dict__
      assert Option('-d').longName == '--default'
  
  def test_corner_case_of_self_with_default(self):
      Option = fixture(lambda self='<self>', shortName='-a': None)
      
      print repr(Option('-a'))
      
      assert repr(Option('-a')) == "Option{shortName='-a'}" # modified
      assert repr(Option('-b')) == "Option{shortName='-b'}"
      assert 'self' not in Option('-a').__dict__


  def test_varargs_and_kwargs_are_not_allowed(self):
      Option = fixture(lambda self, *args: None)
      raises(ValueError, lambda: Option())

      Option = fixture(lambda self, **kwargs: None)
      raises(ValueError, lambda: Option())
    
  def test_tuple_parameter_unpacking_is_not_allowed(self):
      Option = fixture(lambda self, (one, two): None)
      raises(ValueError, lambda: Option())

