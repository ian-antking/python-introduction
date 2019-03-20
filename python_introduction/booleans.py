import math

def negate(bool1):
  # return the opposite of the boolean
  return not bool1

def truthiness(bool1):
  # return the truthiness of the boolean
  return bool(bool1)

def both(bool1, bool2):
  #return true if both booleans are true
  return bool1 and bool2

def neither(bool1, bool2):
  # return true if neither of the booleans are true
  return not bool1 and not bool2

def either(bool1, bool2):
  # return true if either of the booleans are true
  return bool1 or bool2

def exactly_one(bool1, bool2):
  # return true if exatcly one of the booleans are true
  # not both
  return (bool1 and not bool2) or (not bool1 and bool2)

def is_equal(a, b):
  # return true if a and b are equal
  return a == b

def greater_than(a, b):
  # return true is a is greater than b
  return a > b

def less_than(a, b):
  # return true if a is less than b
  return a < b

def greater_than_or_equal(a, b):
  # return true if a is greater than or equal to b
  return a >= b

def less_than_or_equal(a, b):
  # return true if a is less than or equal to b
  return a <= b

def is_odd(num):
  # return true if the number is odd
  return num % 2 != 0

def is_even(num):
  # return true is the number is even
  return num % 2 == 0

def is_square(num):
  # return true if the number is a square number
  return math.sqrt(num) % 1 == 0

def starts_with(string, char):
  # return true if the first character of the string is the same as char
  return string[0] == char

def is_lower(string):
  # return true if all the letters in the string are lower case
  return string.lower() == string