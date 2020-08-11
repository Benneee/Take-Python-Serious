# Custom exceptions are created for reusability purposes
# All user defined exceptions should inherit from the Python's Exception Class

class NegativeNumbersError(Exception):
  """One or more inputs are negative"""
  pass


def add_positive_numbers(a, b):
  try:
    if a <= 0 or b <= 0:
      raise NegativeNumbersError
  except NegativeNumbersError:
    return "E nor work"


print(add_positive_numbers(-5, -1))
