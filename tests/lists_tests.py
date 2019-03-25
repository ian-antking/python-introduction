import unittest
from python_introduction import lists

class TestLists(unittest.TestCase):
  def test_first_element(self):
    list1 = ['apple', 'bannana', 'pear']
    self.assertEqual(lists.first_element(list1), 'apple')

  def test_last_element(self):
    list1 = ['apple', 'bannana', 'pear']
    self.assertEqual(lists.last_element(list1), 'pear')

  def test_specific_element(self):
    list1 = ['apple', 'bannana', 'pear']
    self.assertEqual(lists.specific_element(list1, 1), 'bannana')

  def test_add_to_list1(self):
    list1 = ['apple', 'bannana', 'pear']
    self.assertEqual(lists.add_to_list(list1, 'orange'), ['apple', 'bannana', 'pear', 'orange'])

  def test_remove_nth_element(self):
    list1 = ['apple', 'bannana', 'pear']
    self.assertEqual(lists.remove_nth_element(list1, 1), ['apple', 'pear'])

  def test_remove_specific_element(self):
    list1 = ['apple', 'bannana', 'pear', 'orange']
    self.assertEqual(lists.remove_specific_element(list1, 'bannana'), ['apple', 'pear', 'orange'])

  def test_to_upper_case(self):
    list1 = ['apple', 'bannana', 'pear']
    self.assertEqual(lists.to_upper_case(list1),['APPLE', 'BANNANA', 'PEAR'])

  def test_number_to_string(self):
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.assertEqual(lists.number_to_strings(list1), ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

  def test_only_even(self):
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.assertEqual(lists.only_even(list1), [2, 4, 6, 8, 10])

  def test_sort(self):
    list1 = ['bannana', 'apple', 'pear', 'orange']
    self.assertEqual(lists.sort(list1), ['apple', 'bannana', 'orange', 'pear'])

  def test_sum(self):
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.assertEqual(lists.sum_numbers(list1), 55)