import math

def add(num1, num2):
  # add the two numbers together and return the result
  return num1 + num2

def subtract(num1, num2):
  # subtract num2 from num1 and return the result
  return num1 - num2

def divide(num1, num2):
  # divide the num1 by num2 and return the result
  return num1 / num2

def quotient(num1, num2):
  # divide num1 by num2 and return the quotient
  # eg. 5 divided by 3, the quotient is 1 because 3 goes into 5 once
  return num1 // num2

def modulus(num1, num2):
  # divide num1 by num2 and return the modulus
  # eg. 5 divided by 3, the modulus is 2 because the remainder is 2
  return num1 % num2

def power(num1, num2):
  # multiply num1 but the power of num2 and return the result
  return num1 ** num2

def square_root(num):
  # return the suqare root of the number
  return math.sqrt(num)

def round_to_nearest(num):
  # round the number to the nearest integer and return the result
  return round(num)

def round_down(num):
  # round the number down ad return the result
  return math.floor(num)

def round_up(num):
  # round the number up and return the result
  return math.ceil(num)

def absolute_value(num):
  # return the absolute value of the number
  # eg. the absolute value of -1 is 1
  return abs(num)
