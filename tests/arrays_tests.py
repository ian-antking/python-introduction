import unittest
from python_introduction import arrays

class TestArrays(unittest.TestCase):
  def test_first_element(self):
    array = ['apple', 'bannana', 'pear']
    self.assertEqual(arrays.first_element(array), 'apple')

  def test_last_element(self):
    array = ['apple', 'bannana', 'pear']
    self.assertEqual(arrays.last_element(array), 'pear')

  def test_specific_element(self):
    array = ['apple', 'bannana', 'pear']
    self.assertEqual(arrays.specific_element(array, 1), 'bannana')

  def test_add_to_array(self):
    array = ['apple', 'bannana', 'pear']
    self.assertEqual(arrays.add_to_array(array, 'orange'), ['apple', 'bannana', 'pear', 'orange'])

  def test_remove_nth_element(self):
    array = ['apple', 'bannana', 'pear']
    self.assertEqual(arrays.remove_nth_element(array, 1), ['apple', 'pear'])

  def test_remove_specific_element(self):
    array = ['apple', 'bannana', 'pear', 'orange']
    self.assertEqual(arrays.remove_specific_element(array, 'bannana'), ['apple', 'pear', 'orange'])

  def test_to_upper_case(self):
    array = ['apple', 'bannana', 'pear']
    self.assertEqual(arrays.to_upper_case(array),['APPLE', 'BANNANA', 'PEAR'])

  def test_number_to_string(self):
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.assertEqual(arrays.number_to_strings(array), ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

  def test_only_even(self):
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.assertEqual(arrays.only_even(array), [2, 4, 6, 8, 10])

  def test_sort(self):
    array = ['bannana', 'apple', 'pear', 'orange']
    self.assertEqual(arrays.sort(array), ['apple', 'bannana', 'orange', 'pear'])

  def test_sum(self):
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.assertEqual(arrays.sum_numbers(array), 55)