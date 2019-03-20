import unittest
from python_introduction import booleans

class TestBooleans(unittest.TestCase):
  def test_negate(self):
    self.assertEqual(booleans.negate(True), False)