# The dunder init method is used to set up instantiation logic for each object created from our class
# This method will run automatically whenever an object is instantiated from the class

class Guitar():
  '''The dunder init method'''
  # Sets the initial state of each object
  # It requires at least one parameter
  # It should not return anything

  # The parameter will represent the object that will be created - self
  def __init__(self):
    print(f'A new guitar is being created. This object is {self}')

# By instantiating this new object off our Guitar class, the dunder init method runs first
acoustic = Guitar()
print(acoustic)