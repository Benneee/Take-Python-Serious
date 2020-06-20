from functools import wraps

def be_nice(fn):
  @wraps(fn)
  def inner(*args, **kwargs):
    print('So I am going to run your function next')
    result = fn(*args, **kwargs)
    print('That was fun, you are welcome!')
    return result
  return inner

@be_nice
def complex_business_sum(a, b):
  "Adds the values passed in together"
  return a + b


# When we pass in the function complex_business_sum to the help method
# The string in the method is printed out as the function's documentation
help(complex_business_sum)


# However, if we allow the function to remain wrapped by the decorator,
# the documentation will not be printed until a method from the functools library is used
# The wraps method help the documentation in our complex_business_sum method be recognised by the help method
