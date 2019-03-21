import unittest
from python_introduction import arrays

class TestArrays(unittest.TestCase):
  def test_first_element(self):
    array = ['apple', 'bannana', 'pear']
    self.assertEqual(arrays.first_element(array), 'apple')