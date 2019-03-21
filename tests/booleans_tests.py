import unittest
from python_introduction import booleans

class TestBooleans(unittest.TestCase):
  def test_negate_1(self):
    self.assertEqual(booleans.negate(True), False)

  def test_negate_2(self):
    self.assertEqual(booleans.negate(False), True)

  def test_truthiness_1(self):
    self.assertEqual(booleans.truthiness(''), False)
  
  def test_truthiness_2(self):
    self.assertEqual(booleans.truthiness(0), False)

  def test_truthiness_3(self):
    self.assertEqual(booleans.truthiness([]), False)

  def test_both_1(self):
    self.assertEqual(booleans.both(True, True), True)

  def test_both_2(self):
    self.assertEqual(booleans.both(True, False), False)

  def test_neither_1(self):
    self.assertEqual(booleans.neither(True, False), False)

  def test_neither_2(self):
    self.assertEqual(booleans.neither(False, False), True)

    def test_neither_3(self):
      self.assertEqual(booleans.neither(True, True), False)

  def test_either_1(self):
    self.assertEqual(booleans.either(True, False), True)

  def test_either_2(self):
    self.assertEqual(booleans.either(False, False), False)

  def test_exactly_one_1(self):
    self.assertEqual(booleans.exactly_one(True, False), True)

  def test_exactly_one_2(self):
    self.assertEqual(booleans.exactly_one(True, True), False)

  def test_is_equal_1(self):
    self.assertEqual(booleans.is_equal(1, 1), True)

  def test_is_equal_2(self):
    self.assertEqual(booleans.is_equal(1, 'one'), False)

  def test_greater_than_1(self):
    self.assertEqual(booleans.greater_than(1, 3), False)
  
  def test_greater_than_2(self):
    self.assertEqual(booleans.greater_than(3, 2), True)

  def test_less_than_1(self):
    self.assertEqual(booleans.less_than(1, 3), True)
  
  def test_less_than_2(self):
    self.assertEqual(booleans.less_than(3, 2), False)

  def test_greater_or_equal_1(self):
    self.assertEqual(booleans.greater_than_or_equal(2, 2), True)
  
  def test_greater_or_equal_2(self):
    self.assertEqual(booleans.greater_than_or_equal(2, 1), True)

  def test_greater_or_equal_3(self):
    self.assertEqual(booleans.greater_than_or_equal(1, 2), False)

  def test_less_or_equal_1(self):
    self.assertEqual(booleans.less_than_or_equal(2, 2), True)
  
  def test_less_or_equal_2(self):
    self.assertEqual(booleans.less_than_or_equal(2, 1), False)

  def test_less_or_equal_3(self):
    self.assertEqual(booleans.less_than_or_equal(1, 2), True)

  def test_is_odd_1(self):
    self.assertEqual(booleans.is_odd(3), True)

  def test_is_odd_2(self):
    self.assertEqual(booleans.is_odd(2), False)

  def test_is_even_1(self):
    self.assertEqual(booleans.is_even(3), False)

  def test_is_even_2(self):
    self.assertEqual(booleans.is_even(2), True)

  def test_is_square_1(self):
    self.assertEqual(booleans.is_square(16), True)

  def test_is_square_2(self):
    self.assertEqual(booleans.is_square(10), False)

  def test_starts_with_1(self):
    self.assertEqual(booleans.starts_with('Hello', 'h'), False)

  def test_starts_with_2(self):
    self.assertEqual(booleans.starts_with('Hello', 'H'), True)

  def test_starts_with_3(self):
    self.assertEqual(booleans.starts_with('Hello', 3), False)

  def test_is_lower_1(self):
    self.assertEqual(booleans.is_lower('hello'), True)

  def test_is_lower_2(self):
    self.assertEqual(booleans.is_lower('Hello'), False)