# The nonlocal keyword causes a variable to be globally known
# It however works only within an enclosing function

def outer():
  maggi_type = 'Knorr'

  def inner():
    # The nonlocal
    nonlocal maggi_type
    maggi_type = 'Star'


  inner()

  return maggi_type

print(outer())
