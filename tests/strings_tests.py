import unittest
from python_introduction import strings

class TestStrings(unittest.TestCase):
  def test_say_hello(self):
    self.assertEqual(strings.say_hello('World'), 'Hello, World!')

  def test_say_hello_2(self):
    self.assertEqual(strings.say_hello('Wisconsin'), 'Hello, Wisconsin!') 

  def test_concatenate(self):
    self.assertEqual(strings.concatenate('foo', 'bar'), 'foobar')

  def test_upper_case(self):
    self.assertEqual(strings.upper_case('foobar'), 'FOOBAR')

  def test_lower_case(self):
    self.assertEqual(strings.lower_case('FOOBAR'), 'foobar')

  def test_string_length(self):
    self.assertEqual(strings.string_length('foobarr'), 7)

  def test_first_character(self):
    self.assertEqual(strings.first_character('foobar'), 'f')

  def test_last_character(self):
    self.assertEqual(strings.last_character('foobar'), 'r')

  def test_specific_character(self):
    self.assertEqual(strings.specific_character('foobar', 3), 'b')
if __name__ == '__main__':
  unittest.main(verbosity=2)