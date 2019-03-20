import unittest

from tests import strings_tests
from tests import numbers_tests

def strings_suite():
  suite = unittest.TestSuite()
  result = unittest.TestResult()

  # strings tests
  suite.addTest(unittest.makeSuite(strings_tests.TestStrings))

  runner = unittest.TextTestRunner(verbosity=2)
  print(runner.run(suite))

def numbers_suite():
  suite = unittest.TestSuite()
  result = unittest.TestResult()

  # numbers tests
  suite.addTests(unittest.makeSuite(numbers_tests.TestNumbers))

  runner = unittest.TextTestRunner(verbosity=2)
  print(runner.run(suite))
 
if __name__ == '__main__': 
  # strings_suite()
  # numbers_suite()
  print('Uncomment test suites in test.py to run')
