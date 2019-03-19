def say_hello(string):
  # concatenate the string to the word "Hello, " and add an exclamation on the end
  # say_hello('worlds') should return "Hello, world!"
  return 'Hello, ' + string + '!'

def concatenate(string1, string2):
  # concatenate the two strings together and return the result
  return string1 + string2

def upper_case(string):
  # convert all the letters in the string to upper case and return the result
  return string.upper()

def lower_case(string):
  # convert all the letters in the string to lower case and return the result
  return string.lower()

def string_length(string):
  # return the length (number of characters) in the string
  return len(string)

def first_character(string):
  # return the first character of the string
  return string[0]

def last_character(string):
  # return the last character of the string
  return string[-1]

def specific_character(string, index):
  # return the character of the string stored in the index variable
  return string[index]
