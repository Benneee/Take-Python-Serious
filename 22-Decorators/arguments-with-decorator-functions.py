def be_nice(fn):
  def inner(*args, **kwargs):
    print('So I am going to run your function next')
    # print(args)
    # print(kwargs)

    # At this point, the arguments are de-structured into the function as normal arguments and not as tuples or dictionaries collected from the args and kwargs
    fn(*args, **kwargs)
    print('That was fun, you are welcome!')

  return inner

@be_nice
def complex_business_logic(stakeholder, position):
  print(f'Something complex for {position} {stakeholder}!')

complex_business_logic(stakeholder="Boris", position="CEO")
complex_business_logic("Boris", "CEO")

# To allow for arguments, the argument needs to be passed into the decorator function

