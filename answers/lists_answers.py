def first_element(data):
  # return the first element of the data
  return data[0]

def last_element(data):
  # return the last element of the data
  return data[-1]

def specific_element(data, index):
  # return the element of the data specified in the index
  return data[index]

def add_to_list(data, element):
  # add the element to the end of the data and return it
  data.append(element)
  return data

def remove_nth_element(data, index):
  # removed the element at the position specified in the inded and return the data
  data.pop(index)
  return data

def remove_specific_element(data, element):
  # remove the element from the data
  data.remove(element)
  return data

def number_to_strings(numbers):
  # convert the numbers in the data to strings and return them as a new data

  # advanced answer
  # return [str(number) for number in numbers]

  # basic answer
  strings = []
  for number in numbers:
    strings.append(str(number))
  return strings

def to_upper_case(strings):
  # convert the strings in the data to uppercase

  # advanced answer
  # return [string.upper() for string in strings]

  # basic answer
  upper_strings = []
  for string in strings:
    upper_strings.append(string.upper())
  return upper_strings

def only_even(numbers):
  # return a make a new list from the data with only even numbers

  # advanced answer
  # return [number for number in numbers if number % 2 == 0]

  # basic answer
  even_numbers = []
  for number in numbers:
    if number % 2 == 0:
      even_numbers.append(number)
  return even_numbers

def sort(strings):
  # return the data with the strings sorted into alphabetical order
  strings.sort()
  return strings

def sum_numbers(numbers):
  # return the total of all the numbers in the data
  return sum(numbers)