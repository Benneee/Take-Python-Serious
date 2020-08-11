def divide_five_by_number(n):
  try:
    # The try block executes first
    calculation = 5/n
  # except ZeroDivisionError:
    # because explicit is better than implicit, we can define except blocks by python error classes
    # If the error encountered isn't defined, the except block is not entered
    # If there is an exception from the code in the try block, this block runs
    # return "You cannot divide by zero!"

  # Another specific error definition
  # except TypeError as error:
    # To get the custom error provided by Python when we run into a type error,
    # ... we can assign the error to a variable and pass it as part of our return value as below
    # return f"Invalid object provided: {error}"

  # A neater approach to have multiple error cases
  except(ZeroDivisionError, TypeError) as error:
    return f"Something went wrong. Error: {error}"
  return calculation


print(divide_five_by_number(0))
print(divide_five_by_number(10))
print(divide_five_by_number("nonsense"))
