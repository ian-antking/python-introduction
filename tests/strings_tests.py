import unittest
import strings

class TestSayHello(unittest.TestCase):
  # test the say_hello function
  def test_strings(self):
    # test basic string concatenation
    result = strings.say_hello('world')
    self.assertEqual(result, 'Hello, world!')

if __name__ == '__main__':
  unittest.main()