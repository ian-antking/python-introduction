import unittest

from tests import strings_tests

def strings_suite():
  suite = unittest.TestSuite()
  result = unittest.TestResult()

  # strings tests
  suite.addTest(unittest.makeSuite(strings_tests.TestStrings))

  runner = unittest.TextTestRunner(verbosity=2)
  print(runner.run(suite))
 
if __name__ == '__main__': 
  strings_suite()
