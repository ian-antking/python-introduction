import unittest
from python_introduction import numbers
class TestNumbers(unittest.TestCase):
  def test_add_integers(self):
    self.assertEqual(numbers.add(2, 2), 4)

  def test_add_floats(self):
    self.assertEqual(numbers.add(2.5, 3), 5.5)

  def test_subtract_positive(self):
    self.assertEqual(numbers.subtract(5, 2), 3)

  def test_subtract_negative(self):
    self.assertEqual(numbers.subtract(-2, -3), 1)

  def test_divide(self):
    self.assertEqual(numbers.divide(6, 2), 3)

  def test_divide_float(self):
    self.assertEqual(numbers.divide(5, 2), float(2.5))

  def test_modulus(self):
    self.assertEqual(numbers.modulus(5, 2), 1)
  
  def test_power_square(self):
    self.assertAlmostEqual(numbers.power(5, 2), 25)

  def test_power_cube(self):
    self.assertEqual(numbers.power(3, 3), 27)

  def test_power_indicies(self):
    self.assertEqual(numbers.power(33, 33), 33 ** 33)

  def test_square_root(self):
    self.assertEqual(numbers.square_root(4), 2)

  def test_round_to_nearest(self):
    self.assertEqual(numbers.round_to_nearest(float(2.5)), 2)

  def test_round_up(self):
    self.assertEqual(numbers.round_up(float(2.5)), 3)

  def test_round_down(self):
    self.assertEqual(numbers.round_down(float(2.5)), 2)

  def test_absolute_value(self):
    self.assertEqual(numbers.absolute_value(-1), 1)
  

if __name__ == '__main__':
  unittest.main(verbosity=2)