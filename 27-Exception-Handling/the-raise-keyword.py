def add_positive_numbers(a, b):
  try:
    if a <= 0 or b <= 0:
      # ValueError is raised when the right type of the needed value is provided but an inappropriate value
      # That's what happens when a negative number is provided in place of positive number.
      # The raise keyword is used to trigger errors when necessary
      raise ValueError('One or both of the values is invalid. Both numbers must be positive')
    # A custom error message can be provided as an argument to the error provided
    return a + b
  except ValueError as error:
    return f"{error}"



print(add_positive_numbers(9, 7))
print(add_positive_numbers(9, -7))
