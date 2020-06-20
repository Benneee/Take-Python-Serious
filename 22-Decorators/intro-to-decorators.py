# A decorator enhances the features of a function without changing its core functionality
# A decorator is a higher-order function that takes in a function as an argument and returns
# ... another function as a return value

def be_nice(fn):
  def inner():
    print('So I am going to run your function next')
    fn()
    print('That was fun, you are welcome!')

  return inner


# A sample function we want to decorate
# def complex_business_logic():
#   print('Something complex!')

# be_nice(complex_business_logic)()

# The syntax for introducing the decorator to the complex_business_logic is the @ sign
# Instead of passing the function to the be_nice decorator as a function, we can use the method below
@be_nice
def complex_business_logic():
  print('Something complex!')

complex_business_logic()

# The decorator can be used with multiple functions
