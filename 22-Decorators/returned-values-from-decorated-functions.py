def be_nice(fn):
  def inner(*args, **kwargs):
    print('So I am going to run your function next')
    # When the function to be run inside the decorator has to return a value,
    # We can assign the function to a variable to preserve it and return it after this decorator
    # ... executes
    result = fn(*args, **kwargs)
    print('That was fun, you are welcome!')
    return result
  return inner

@be_nice
def complex_business_sum(a, b):
  # print(f'Something complex for {position} {stakeholder}!')
  return a + b

# print(complex_business_sum(5, 7))
print(complex_business_sum(a=5, b=7))
