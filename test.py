import unittest

from tests import strings_tests, numbers_tests, booleans_tests, lists_tests

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

def booleans_suite():
  suite = unittest.TestSuite()
  result = unittest.TestResult()

  # boolean tests
  suite.addTests(unittest.makeSuite(booleans_tests.TestBooleans))

  runner = unittest.TextTestRunner(verbosity=2)
  print(runner.run(suite))

def lists_suite():
  suite = unittest.TestSuite()
  result = unittest.TestResult()

  # array tests
  suite.addTests(unittest.makeSuite(lists_tests.TestLists))

  runner = unittest.TextTestRunner(verbosity=2)
  print(runner.run(suite))
 
if __name__ == '__main__': 
  # REMOVE THE # FROM THE LINES BELOW TO RUN TESTS 

  # strings_suite()
  # numbers_suite()
  # booleans_suite()
  # lists_suite()
  print('Uncomment test suites in test.py to run')
