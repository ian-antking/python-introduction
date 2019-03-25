import unittest
from python_introduction import lists

class TestLists(unittest.TestCase):
  def test_first_element(self):
    data = ['apple', 'bannana', 'pear']
    self.assertEqual(lists.first_element(data), 'apple')

  def test_last_element(self):
    data = ['apple', 'bannana', 'pear']
    self.assertEqual(lists.last_element(data), 'pear')

  def test_specific_element(self):
    data = ['apple', 'bannana', 'pear']
    self.assertEqual(lists.specific_element(data, 1), 'bannana')

  def test_add_to_list(self):
    data = ['apple', 'bannana', 'pear']
    self.assertEqual(lists.add_to_list(data, 'orange'), ['apple', 'bannana', 'pear', 'orange'])

  def test_remove_nth_element(self):
    data = ['apple', 'bannana', 'pear']
    self.assertEqual(lists.remove_nth_element(data, 1), ['apple', 'pear'])

  def test_remove_specific_element(self):
    data = ['apple', 'bannana', 'pear', 'orange']
    self.assertEqual(lists.remove_specific_element(data, 'bannana'), ['apple', 'pear', 'orange'])

  def test_to_upper_case(self):
    data = ['apple', 'bannana', 'pear']
    self.assertEqual(lists.to_upper_case(data),['APPLE', 'BANNANA', 'PEAR'])

  def test_number_to_string(self):
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.assertEqual(lists.number_to_strings(data), ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

  def test_only_even(self):
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.assertEqual(lists.only_even(data), [2, 4, 6, 8, 10])

  def test_sort(self):
    data = ['bannana', 'apple', 'pear', 'orange']
    self.assertEqual(lists.sort(data), ['apple', 'bannana', 'orange', 'pear'])

  def test_sum(self):
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.assertEqual(lists.sum_numbers(data), 55)