# An else block will run only if the try block executes without an error
# The finally block will run regardless if there was an exception in the try block
# Finally is usually used to tie up loose ends in our program

x = 10

try:
  print(x + 5)
except NameError:
  print("Some variable is not defined")
else:
  print("I only show if there is no error in the try block")
finally:
  print("I run regardless of an error in the try block")
